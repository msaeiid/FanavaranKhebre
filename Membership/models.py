from django.db import models
from django.contrib.auth.models import User
from Library.models import *


class Person(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    type_choices = (("member", "Member"),
                    ("librarian", "Librarian"))
    type = models.CharField(max_length=11, choices=type_choices, default='member')

    def __str__(self):
        return self.user.get_full_name()
# Create your models here.
