from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import HomePage, testPage, get_name,borrow_page, my_borrows, view_borrow_reqs, lend_book, view_lent_books, recieve_book, about_us

urlpatterns =[
    path('home/', HomePage, name='home'),
    path('test/', get_name,name = 'test'),
    path('borrow/', borrow_page, name = 'borrowpage'),
    path('my_borrows/',my_borrows, name = 'my_borrows'),
    path('view_borrow_reqs/', view_borrow_reqs, name = 'view_borrow_reqs'),
    path('lend_book/', lend_book, name = 'lend_book'),
    path('view_lent_books/', view_lent_books, name = 'view_lent_books'),
    path('receive_book/', recieve_book, name='recieve_book'),
    path('about_us', about_us, name='about_us')
]