from .models import Profile, Book
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms



class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        exclude = ('user',)
        fields= '__all__' 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)
        fields= '__all__' 

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

