from django.db import models

# Create your models here.
class book(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.TextField()
    genre = models.TextField()
    department = models.TextField()
    vendor = models.TextField()
    publisher = models.TextField()
    vendor_id = models.IntegerField()
    publisher_id = models.IntegerField()
    count = models.IntegerField()


