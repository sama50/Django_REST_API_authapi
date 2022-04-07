from django.urls import path 
from api.views import UserRegistrationView , UserLoginView , UserProfileView,ChangePasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change/', ChangePasswordView.as_view(), name='chnage'),
]
