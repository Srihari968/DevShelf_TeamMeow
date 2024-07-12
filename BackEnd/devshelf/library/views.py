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
from user.models import Borrowed, User
from datetime import datetime, timedelta



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
    return render(request,template_name='login.html')


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


    return render(request, 'library/search.html', context)



def borrow_page(request):
    print("dsdsds")
    print(request.POST)
    for x in request.POST:
        print(x)
        print(request.POST[x])
    context = {'borrowed': request.POST.get('borrow', ""), 'username': request.POST.get('username', "")}
    borrow_book(request.POST.get('borrow', ""), request.POST.get('username', ""))
    return render(request, 'library/borrowpage.html', context)
def my_borrows(request):
    all_borrowals = Borrowed.objects.all()
    my_borrowals = []

    for x in all_borrowals:
        if x.user.username == request.POST['username']:
            my_borrowals.append(x)
    users = User.objects.all()
    userr = None
    for x in users:
        if x.username == request.POST['username']:
            print("sssssssssssssss")
            userr = x

    context = {'my_borrowals': my_borrowals, 'username': request.POST['username'], 'user': userr}
    return render(request, 'library/my_borrows.html', context)

def view_borrow_reqs(request):
    all_borrowals = Borrowed.objects.all()
    active_borrow_reqs = []
    for x in all_borrowals:
        if x.borrowed == True and x.is_lent == False:
            active_borrow_reqs.append(x)
    context = {'username': request.POST['username'], 'borrowals': active_borrow_reqs}
    return render(request,'library/lend_borrows.html', context)

def lend_book(request):
    print(request.POST['lend_id'])
    all_borrowals = Borrowed.objects.all()
    for x in all_borrowals:
        if str(x.id) == str(request.POST['lend_id']):
            print("found")
            x.is_lent = True
            x.borrowed_time = datetime.now()
            x.return_time = datetime.now() + timedelta(days= 7)

            books = Book.objects.all()
            for b in books:
                if b.title == x.book.title:
                    # b.count = b.count - 1
                    b.save()
                    break
            x.save()
    context = {'username' : request.POST['username']}
    return render(request,'library/HomePage.html', context)

def view_lent_books(request):
    all_borrowals = Borrowed.objects.all()
    receivable_borrowals = []
    # if request.method == 'POST':
    #     for x in all_borrowals:
    #         if str(x.id) == str(request.POST['borrowal_id']):
    #             x.is_lent = False
    #             x.borrowed = False
    #             books = Book.objects.all()
    #             for book in books:
    #                 if book.title == x.book.title:
    #                     book.count = book.count+1
    #                     book.save()
    #                     break
    #             x.save()
    #             break
    #     context = {'username': request.POST['username']}
    #     return render(request,'HomePage.html', context)
    for x in all_borrowals:
        if x.is_lent == True:
            receivable_borrowals.append(x)
    context = {'lents': receivable_borrowals, 'username': request.POST['username']}
    return render(request, 'library/receive_book.html', context)

def recieve_book(request):
    all_borrowals = Borrowed.objects.all()
    if request.method == 'POST':
        for x in all_borrowals:
            if str(x.id) == str(request.POST['borrowal_id']):
                x.is_lent = False
                x.borrowed = False
                books = Book.objects.all()
                for book in books:
                    if book.title == x.book.title:
                        book.count = book.count+1
                        book.save()
                        break
                x.save()
                break
        context = {'username': request.POST['username']}
    return render(request,'library/HomePage.html', context)






