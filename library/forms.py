from django import forms

from .models import Profile, Book


class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        fields=['name','profilepic','email','bio'] 

class BookForm(forms.ModelForm):
  
    class Meta:
        model = Book
        fields=['image','title','author','synopsis','location'] 