from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import HomePage, testPage, get_name,borrow_page, my_borrows, lend_books

urlpatterns =[
    path('home/', HomePage, name='home'),
    path('test/', get_name,name = 'test'),
    path('borrow/', borrow_page, name = 'borrowpage'),
    path('my_borrows/',my_borrows, name = 'my_borrows'),
    path('lend_books/', lend_books, name = 'lend_books')
]