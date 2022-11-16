from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

def submit(request):
    form = BookForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect ('index')
    
    else:
        form = BookForm()

    return render(request, 'submit.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')

def signup(request):
    return render(request, 'registration/signup.html')
