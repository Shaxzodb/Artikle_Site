from django.urls import path
from .views import CreateViewPost

urlpatterns = [
    path('users/',CreateViewPost.as_view(),name='singup')
]
