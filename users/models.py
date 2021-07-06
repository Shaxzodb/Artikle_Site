from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CreateUserViews(AbstractUser):
    email=models.EmailField('Email')
    manzil=models.CharField('Manzil',max_length=256)
