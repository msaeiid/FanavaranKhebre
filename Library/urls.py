"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from Library import views

app_name = 'library'

urlpatterns = [
    path('book/list/', views.get_book_search, name='book_list'),
    path('order/add/<int:book_id>', views.order_add, name="order_book"),
    path('order/list', views.order_list, name="my_order_list"),
    path('order/remove/<int:order_id>', views.order_remove, name="order_remove")
]
