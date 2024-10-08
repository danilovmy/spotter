from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  #TokenVerifyView
from .api import RegisterApiView
from django.urls import path

# Create your views here.
urlpatterns = [
    path('user/register', RegisterApiView.as_view(), name='user_register'),
    path('user/login', TokenObtainPairView.as_view(), name='user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='user_token_refresh'),
    # path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]
