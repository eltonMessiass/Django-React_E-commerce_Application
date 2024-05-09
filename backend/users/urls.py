from .views import CreateUserView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]