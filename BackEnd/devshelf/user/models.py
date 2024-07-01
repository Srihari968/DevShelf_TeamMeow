from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # AbstractUser contains username, email, is_staff
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'phone']
    
    def __str__(self):
        return self.name
