from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render

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
            if x.name == request.POST['username'] and request.POST['password'] == 'hello':
                context = {'username': x.name}
                return render(request, 'library/HomePage.html', context)

    return render(request, template_name='first.html')


