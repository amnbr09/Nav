from django import forms
from models import Viewers
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = Viewers
         fields = ('profile_pic')