"""
    User view file, includes (views, part-authentication)
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from .serializer import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# custom class imports
from User.models import User
from User.serializer import UserSerializer


class CreateUserView(APIView):
    """Handles all the view routes for the user
    """
    permission_classes = [AllowAny]

    # method handles creating a user
    def post(self, request):
        """creates a user """

        # deserialize data from the request object        
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsView(APIView):
    """get, updates, and deletes user object
    """
    permission_classes = [IsAuthenticated]

    # create a get http method that fetches a particular user object
    def get(self, request, user_id):
        """gets a user by id
        """
        try:
            user = User.objects.get(pk=user_id)
            deserialized = UserSerializer(user)

            return Response(
            deserialized.data, status=status.HTTP_200_OK )

        except User.DoesNotExist:
            return Response(
                deserialized.errors, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        """updates a user instance
        """
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
    
            return Response(
                {
                    "success_message": "successfully updated user",
                    "user": serializer.data
                    }, 
                status=status.HTTP_201_CREATED, )
    
        return Response(
            {"error_message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk=None):
        """deletes a user by pk
        """
        try:
           user = User.objects.get(request.user, pk=pk)
           user.delete()
           return Response(
               {"success": "User successfully deleted"}
           )
        except Exception as e:
            return Response(
                {"error": f'{e}'}
            )

# create UserListiVIew
class UsersListView(APIView):
    """List all the users in the storage
    """
    permission_classes = [AllowAny]
    def get(self, request):
        """fetches all user data fro the database
        """

        try:
            all_user_serializer = User.objects.all()
            serializer = UserSerializer(all_user_serializer, many=True)
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error_message': str(e)}, status=status.HTTP_404_NOT_FOUND)


class LoginView(APIView):
    """obtains view sets cookie to the browser
    """
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        """ handles"""
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data.get('user')

            if user is None:
                return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            response = Response({
                "user": UserSerializer(user).data,
                "message": "login successful"
            }, status=status.HTTP_200_OK)

            response.set_cookie(key='access_token', 
                                value=access, httponly=True, 
                                secure=False, samesite=None,
                                max_age=15*60)
            
            response.set_cookie(key='refresh_token', 
                                value=str(refresh), httponly=True, 
                                secure=False, samesite=None,
                                max_age=7*24*60*60
                            )
            return response
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST
                        )


# verify login from frontend
class VerifyLoginState(APIView):
    """checks if user is logged in
    """

    def get(self, request):
        token = request.COOKIES.get('access_token')

        if not token:
            return Response(
                { "is_authenticated": False,
                  "message": "user is not authenticated"
                }, status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            { "is_authenticated": True,
              "user": {
                "id": request.user.id,
                "email": request.user.email
              }
            }
        )


class LogoutView(APIView):
    """logout user
    """

    def post(self, request):
        """Makes a request to logout user
        """
        
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()

            except Exception as e:
                return Response(
                    {"error": f"An error occurred: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        response = Response(
            {"message": "logout successful"},
            status=status.HTTP_200_OK
        )
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response

