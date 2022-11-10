from random import lognormvariate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from Library import models
from Library.models import Book, Order


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    context_object_name = "books"
    template_name = "Library/list.html"


@login_required
def order_add(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.is_order_allowed:
        order = Order(book=book, person=request.user.person)
        order.save()
        return redirect(reverse('library:book_list'))


@login_required
def order_list(request):
    context = {}
    user_order_list = Order.objects.filter(person=request.user.person)
    if user_order_list.count() > 0:
        context["my_order"] = user_order_list
    return render(request, template_name='Library/order_list.html', context=context)


@login_required
def order_remove(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.person == order.person and order.state == "approved":
        order.state = "return"
        order.save()
        return redirect(reverse("library:my_order_list"))
    else:
        return HttpResponseNotFound("person who requested this book is not  equal to logged in user")
