"""
    User view file, includes (views, part-authentication)
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from .serializer import CustomTokenObtainPairSerializer
from django.views.decorators.csrf import csrf_exempt


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


class CustomTokenObtainView(TokenObtainPairView):
    """obtains view sets cookie to the browser
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # obtain response object from the made request
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            data = {
                'message': "successfully logged in",
                'status': status.HTTP_200_OK,
            }

            # set cookies
            response.set_cookie(
                "access_token", access_token,
                httponly=True,
                secure=True,
                samesite=None,
                max_age=7 * 24 * 60 * 60  # 7 days
                )
            response.set_cookie(
                "refresh_token", refresh_token,
                httponly=True,
                secure=True,
                samesite=None,
                max_age=7 * 24 * 60 * 60  # 7 days
                )

            del response.data['access']
            del response.data['refresh']

            return response
        else:
            response.data = {
                'message': 'Invalid credentials',
                'status': status.HTTP_401_UNAUTHORIZED
            }
            return response


class CustomTokenRefreshView(TokenRefreshView):
    """refreshes the token and provide new access token
    """

    def post(self, request, *args, **kwargs):
        # get the refresh-token from the request
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({
                'error': 'No refresh token found!'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # add the refresh token to the request data
        request.data['refresh_token'] = refresh_token

        # get new access token
        res = super().post(request, *args, **kwargs)

        if res.status_code == 200:
            new_access_token = res.data.get('access')

            res.set_cookie(
                "refresh_token",
                new_access_token,
                httponly=True,
                samesite=None,
                max_age=15 * 60
            )
            del res.data['access']
        return res


# logout view
class Logout(APIView):
    """Logs user out
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """send the token to be removed
        """
        print('User is', request.user)
        

        response = Response({"message": "logged out"}, status=status.HTTP_200_OK)

        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response


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
