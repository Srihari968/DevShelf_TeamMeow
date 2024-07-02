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


        context = {'search': search, 'books': books}


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/library/test/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', context)