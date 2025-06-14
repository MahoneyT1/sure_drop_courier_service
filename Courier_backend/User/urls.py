from django.urls import path
from User import views
from .views import CustomTokenObtainView, CustomTokenRefreshView, Logout, VerifyLoginState
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('auth/user/register/', view=views.CreateUserView.as_view(), name='create-user'),
    path('users/list/', view=views.UsersListView.as_view(), name='list-users'),
    path("user/<str:user_id>/", view=views.UserDetailsView.as_view(), name='update-get-del'),
    path('login/', view=CustomTokenObtainView.as_view(), name='obtain-token'),
    path('token/refresh/', view=CustomTokenRefreshView.as_view(), name='refresh-token'),
    path('token/verify/', view=TokenVerifyView.as_view(), name='verify-token'),
    path('logout/', view=Logout.as_view(), name='logout-view'),
    path('auth-verify/', view=views.VerifyLoginState.as_view(), name='verify-user'),
]
