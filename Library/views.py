from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from Library import models
from Library.models import Book


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    context_object_name = "books"
    template_name = "Library/list.html"
