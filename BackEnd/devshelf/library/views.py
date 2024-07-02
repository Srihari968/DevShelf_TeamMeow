from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import NameForm
from .models import Book


# Create your views here.



def HomePage(request):
    #template = loader.get_template('HomePage.html')
    return render(request,template_name='HomePage.html')
    #return HttpResponse(template.render())
    
    
def testPage(request):
    #template = loader.get_template('HomePage.html')
    return render(request,template_name='first.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    global context
    books = Book.objects.all()


    print(books)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        search = request.POST['your_name']
        print('Entered ', search)

        new = []
        for book in books:
            if search.lower() in book.title.lower() or search.lower() in book.author.lower() or search.lower() in book.genre.lower() or search.lower() in book.department.lower():
                new.append(book.title)

        context = {'search': search, 'books': new}
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', context)