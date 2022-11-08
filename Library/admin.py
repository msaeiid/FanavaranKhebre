from django.contrib import admin
from Library.models import Writer, Category, Book

# Register your models here.

admin.site.register(Writer)
admin.site.register(Category)
admin.site.register(Book)
