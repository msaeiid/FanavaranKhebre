from django.contrib import admin
from Library.models import Writer, Category, Book, Order


# Register your models here.


class OrderCustom(admin.ModelAdmin):
    list_display = ("person", "book", "state",)


class BookCutom(admin.ModelAdmin):
    list_display = ("title", "writer", "quantity", "category")


admin.site.register(Writer)
admin.site.register(Category)
admin.site.register(Book, BookCutom)
admin.site.register(Order, OrderCustom)
