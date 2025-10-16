"""
    User authentication class
"""
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed


class CookieAuthentication(JWTAuthentication):
    """authenticate and validates user's tokens
    """
    
    def authenticate(self, request):
        """authenticates login
        """

        # get the access token from the cookie
        access_token = request.COOKIES.get('access_token')

        if not access_token:
            return None
        
        try:
            # validate the obtainedtoken
            validated_token = self.get_validated_token(access_token)
        except Exception:
            # Don't raise here — return None so that views like the login
            # endpoint can still be reached even if the client sent a stale
            # or invalid cookie. Returning None lets other views handle
            # authentication/permission checks normally.
            return None

        try:
            user = self.get_user(validated_token)
            return (user, validated_token)
        except Exception:
            # Similarly, if user retrieval fails, don't raise an exception
            # at this stage. Return None to treat the request as unauthenticated.
            return None
