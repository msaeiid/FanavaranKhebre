from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Membership.forms import UserRegisterForm


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('membership:login')
    form_class = UserRegisterForm
    success_message = "your account has been created successfully"
    context_object_name = "form"
# Create your views here.
