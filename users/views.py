from django.shortcuts import render
from .forms import UserCreateViws
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
class CreateViewPost(CreateView):
    form_class=UserCreateViws
    template_name='singup.html'
    success_url=reverse_lazy('login')