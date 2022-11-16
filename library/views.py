from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    books = Book.objects.all
    context = {'books':books}
    return render(request,'home.html',context)

def profile(request):
    return render(request, 'profile.html')

def book(request):
    return render(request, 'book.html')

def search(request):
    return render(request, 'search.html')
