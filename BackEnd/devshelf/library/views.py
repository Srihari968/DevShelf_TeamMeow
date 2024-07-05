from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import NameForm
from .models import Book
from .helper import borrow_book
from user.models import Borrowed


# Create your views here.



def HomePage(request):
    #template = loader.get_template('HomePage.html')
    for x in request.POST:
        print(x)
    context
    return render(request,template_name='library/HomePage.html')
    #return HttpResponse(template.render())
    
    
def testPage(request):
    #template = loader.get_template('HomePage.html')
    return render(request,template_name='first.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    global context
    books = Book.objects.all()


    #print(books)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        search = request.POST['your_name']
        for x in request.POST:
            print(x)
        print('Entered ', search)

        new = []
        for book in books:
            if search.lower() in book.title.lower() or search.lower() in book.author.lower() or search.lower() in book.genre.lower() or search.lower() in book.department.lower():
                new.append(book)

        context = {'search': search, 'books': new, 'username': request.POST['username']}
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    return render(request, 'library/search_books.html', context)

def borrow_page(request):
    for x in request.POST:
        print(x)
        print(request.POST[x])
    context = {'borrowed': request.POST['borrow'],'username': request.POST['username']}
    borrow_book(request.POST['borrow'],request.POST['username'])

    return render(request,'library/borrowpage.html',context)
def my_borrows(request):
    all_borrowals = Borrowed.objects.all()
    my_borrowals = []

    for x in all_borrowals:
        if x.user.name == request.POST['username']:
            my_borrowals.append(x)
    context = {'my_borrowals': my_borrowals, 'username': request.POST['username']}
    return render(request, 'library/my_borrows.html', context)

def lend_books(request):
    all_borrowals = Borrowed.objects.all()
    context = {'username': request.POST['username'], 'borrowals': all_borrowals}
    return render(request,'library/lend_borrows.html', context)


