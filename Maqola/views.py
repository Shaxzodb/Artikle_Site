from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .models import Article
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView


class AlerDetailViewsPot(LoginRequiredMixin,DetailView):
    model=Article
    template_name='detail.html'
    login_url='login'
    
class AlerListViewPost(LoginRequiredMixin,ListView):
    model=Article
    template_name='home.html'
    """ context_object_name="Postlar" """
    login_url='login'
class AlerCreateViews(LoginRequiredMixin,CreateView):
    model=Article
    template_name='new.html'
    fields=('title','text','author','kurish')
    success_url=reverse_lazy('article')
    login_url='login'
    

class AlerDeleteViews(LoginRequiredMixin,DeleteView):
    model=Article
    template_name='delete.html'
    fields=('title','text','author','date','kurish')
    success_url=reverse_lazy('article')
    login_url='login'

    
class AlerUpdateViews(LoginRequiredMixin,UpdateView):
    model=Article
    template_name='update.html'
    fields=('title','text','kurish')
    success_url=reverse_lazy('article')
    login_url='login'
    
