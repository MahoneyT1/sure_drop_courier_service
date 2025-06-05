"""
    User authentication class
"""
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTCookieAuthentication(JWTAuthentication):
    """authenticate and validates user's tokens
    """

    def authenticate(self, request):
        """authenticates login
        """

        # get the access token from the cookie
        access_token = request.COOKIES.get('access_token')

        if not access_token:
            return None # continue identifying current user as annonymous user
        
        # validate the obtainedtoken
        validated_token = self.get_validated_token(access_token)

        # get the user from the token
        user = self.get_user(validated_token)

        return (user, validated_token)
