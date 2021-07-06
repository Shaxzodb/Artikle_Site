from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreateViws,UserChangeViews
from .models import CreateUserViews
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=UserCreateViws
    form=UserChangeViews
    model=CreateUserViews
    list_display=['username','email','manzil']
admin.site.register(CreateUserViews,CustomUserAdmin)