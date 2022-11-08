from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Writer(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    writer = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title
