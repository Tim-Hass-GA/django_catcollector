from django import forms
from .models import Cat, Toy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# special extention

# class CatForm(forms.Form):
class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ('name','description','breed','age',)

    # name = forms.CharField(label='Name', max_length=100)
    # description = forms.CharField(label='Description', max_length=250)
    # breed = forms.CharField(label='Breed', max_length=100)
    # age = forms.IntegerField(label='Age')

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('name',)

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(max_length=254,help_text="Email is required")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
