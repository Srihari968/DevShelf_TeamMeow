from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import RegisterView
from .views import login


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', login, name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
