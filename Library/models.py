from django.db import models
from django.contrib.auth.models import User
from Membership.models import *


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
    quantity = models.PositiveIntegerField(default=1)
    person_list = models.ManyToManyField(to=Person, through="Order", related_name="book")

    def __str__(self):
        return self.title

    def number_of_available(self):
        order_count = self.person_list.filter(order__state__in=['new', 'approved']).count()
        return self.quantity - order_count

    def is_order_allowed(self):
        return self.number_of_available() > 0


class Order(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    state_choices = (
        ("new", "New"),
        ("approved", "Approved"),
        ("return", "Return")
    )
    state = models.CharField(max_length=10, choices=state_choices, default="new")
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.user.get_full_name()
