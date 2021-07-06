from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CreateUserViews
class UserCreateViws(UserCreationForm):
    class Meta(UserCreationForm):
        model=CreateUserViews
        fields=UserCreationForm.Meta.fields+('email','manzil')
class UserChangeViews(UserChangeForm):
    class Meta(UserChangeForm):
        model=CreateUserViews
        fields=UserChangeForm.Meta.fields
