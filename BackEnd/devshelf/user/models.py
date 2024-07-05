from django.db import models
from django.contrib.auth.models import AbstractUser
from library.models import Book



class User(AbstractUser):
    # AbstractUser contains username, email, is_staff
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'phone']
    
    def __str__(self):
        return self.name


class Borrowed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    borrow_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField()
    borrowed = models.BooleanField(default=False)
    is_lent = models.BooleanField(default=False)
    
    def __str__(self):
        return str(user.name) + str(book.title)