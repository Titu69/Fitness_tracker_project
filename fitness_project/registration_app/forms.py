from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile_sqll,Profiles_mongo_data
""" class RegisterForm(forms.Form):
    #email = forms.EmailField(required=True)
    class Meta:
        model =Profiles_mongo_data
        fields=['username','email'] """ 
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)
    age = forms.IntegerField()
    weight = forms.FloatField()
    height = forms.FloatField()  
#from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)




