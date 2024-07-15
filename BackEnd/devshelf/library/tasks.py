from django.core.mail import send_mail
from user.models import Borrowed, User
from datetime import datetime, timedelta


def send_submit_mail():
    all_borrows = Borrowed.objects.all()
    for x in all_borrows:
        print(x.user.name)

        if x.borrowed and x.is_lent:
            diff = x.return_time.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)
            day = timedelta(days=1)
            date = str(x.return_time.day) + '/' + str(x.return_time.month) + '/' + str(x.return_time.year)
            if day > diff > timedelta(seconds=0):
                send_mail("Return book to Akshara Library",
                          "Dear " + x.user.name + "\nPlease return " + x.book.title + " to the library.\nThe Due date for returning is : " + date + "\nA fine will be imposed if the book is not returned soon.",
                          "aksharaiitdh@gmail.com",
                          [x.user.email],
                          fail_silently=False
                          )
    return
