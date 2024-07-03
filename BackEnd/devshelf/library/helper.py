from .models import Book

def borrow_book(title: str):
    books = Book.objects.all()
    for x in books:
        if x.title == title:
            x.count = x.count - 1
            x.save()
