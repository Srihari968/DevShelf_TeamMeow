from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import HomePage, testPage, get_name

urlpatterns =[
    path('home/', HomePage, name='home'),
    path('test/',get_name,name = 'test')
]