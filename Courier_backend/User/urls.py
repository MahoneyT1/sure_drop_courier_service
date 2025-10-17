from django.urls import path
from User import views
from .views import LoginView, LogoutView, VerifyLoginState, HealthCheckView
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('/', view=HealthCheckView.as_view(), name='health-check'),
    path('auth/user/register/', view=views.CreateUserView.as_view(), name='create-user'),
    path('users/list/', view=views.UsersListView.as_view(), name='list-users'),
    path("user/<str:user_id>/", view=views.UserDetailsView.as_view(), name='update-get-del'),
    path('login/', view=LoginView.as_view(), name='obtain-token'),
    path('token/verify/', view=TokenVerifyView.as_view(), name='verify-token'),
    path('logout/', view=LogoutView.as_view(), name='logout-view'),
    path('auth-verify/', view=views.VerifyLoginState.as_view(), name='verify-user'),
]
