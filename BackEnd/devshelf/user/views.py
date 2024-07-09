from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponse
from django.template import loader
from .models import User


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]


def login(request):
    users = User.objects.all()
    if(request.method == 'POST'):
        for x in users:
            if x.username == request.POST['username'] and x.check_password(request.POST['password']):
                context = {'username': x.name}
                return render(request, 'library/HomePage.html', context)
        messages.info(request, 'Username/Password are incorrect. Please try again!')

    return render(request, template_name='login.html')

def signup(request):
    if(request.method == 'POST'):
        if len(request.POST['username']) * len(request.POST['name']) * len(request.POST['email']) * len(request.POST['phone_number']) *len(request.POST['password']) == 0:
            messages.info(request, "All fields are necessary")
            return render(request,template_name='SignUp.html')
        new_user = User()
        new_user.username = request.POST['username']
        new_user.name = request.POST['name']
        new_user.email = request.POST['email']
        new_user.phone = request.POST['phone_number']
        if request.POST['password'] == request.POST['confirm_password']:
            new_user.set_password(request.POST['password'])
            new_user.save()
            return render(request,template_name='login.html')
        else:
            messages.info(request,"Password and Confirm Password do not match")
            return render(request,template_name="SignUp.html")
    else:
        return render(request,template_name='SignUp.html')


