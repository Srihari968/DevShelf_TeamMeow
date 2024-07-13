from django.urls import path
from .views import login, signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',signup , name='signup'),
    path('login/', login, name='token_obtain_pair'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/reset_password_form.html'), name='password_reset_confirm'),
    path('reset_password_complete//', auth_views.PasswordResetCompleteView.as_view(template_name='user/reset_password_complete.html'), name='password_reset_complete'),
]
