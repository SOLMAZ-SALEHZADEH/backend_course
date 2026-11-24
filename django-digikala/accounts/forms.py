# form are only for page sites not admin panel 
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

# forms are class base in django and should be inherited from forms.Form
# register
class UserRegisterForm(UserCreationForm):
    #in  UserCreationForm by deafult username,password1,password2 are requierd 
    # other fields such as first_name last_name are set as required field manually in User model
    # so these fields should be defined in meta fields to show in the form
    # add phone field to the form which is not include in UserCreationForm by default
    phone = forms.CharField(max_length=11, label='phone number')

    class Meta():
        # it sets that forms works with user model
        # فرم قرار است یک نمونه از مدل User بسازد
        model= User
        # مشخص می‌کند  چه فیلدهایی در فرم نمایش داده شود
        fields= ['first_name','last_name','phone','password1','password2']


# login
class UserLoginForm(AuthenticationForm):
    # AuthenticationForm provides username and password fields by default.
    # username field is defined again to set restrictions on it
    username = forms.CharField(max_length=11)
    # password = forms.CharField()   