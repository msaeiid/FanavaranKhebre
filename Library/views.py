from random import lognormvariate

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from Library.models import Book, Order


# Create your views here.


@login_required
def get_book_search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        if search is None:
            books = Book.objects.all()
        else:
            books = Book.objects.filter(Q(title__startswith=search) |
                                        Q(subject__startswith=search) |
                                        Q(writer__f_name__startswith=search) |
                                        Q(writer__l_name__startswith=search))
        context = {'books': books}
        return render(request, template_name="Library/list.html", context=context)


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
