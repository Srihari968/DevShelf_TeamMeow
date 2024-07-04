from .models import Book
import os
from user.models import Borrowed, User

from datetime import datetime


def borrow_book(title: str, username:str):

    users = User.objects.all()
    books = Book.objects.all()

    borrowed = Borrowed()
    for x in users:
        if x.name == username:
            borrowed.user = x
    for x in books:
        if x.title == title:
            borrowed.book = x
    borrowed.borrow_time = datetime.now()
    borrowed.return_time = datetime.now()
    borrowed.borrowed = True

    borrowed.save()

    for x in books:
        if x.title == title:
            x.count = x.count - 1
            x.save()
            break
