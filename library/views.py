from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm, ProfileForm, BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout 
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    books = Book.objects.all
    context = {'books':books}
    return render(request,'home.html',context)

@login_required(login_url='login')
def profile(request):
    current_user = request.user
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    books =Book.objects.filter(user_id = current_user.id).all()
    wishlist = Wishlist.objects.filter(user_id = current_user.id).all()


    
    print ('here is our user')
    print (current_user)

    print ('here is their wishlist')
    print (wishlist)
    
    for item in wishlist:
        print(item.user)

    return render(request, 'profile.html', {"current_user":current_user,"books":books,"wishlists":wishlist, "profiles":profiles})

def book(request):
    return render(request, 'book.html')

def search(request):
    return render(request, 'search.html')

@login_required(login_url='login')
def updateprofile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect ('index')
    
    else:
        form = ProfileForm()

    return render(request, 'updateprofile.html', {'form': form})

@login_required(login_url='login')
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


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    

    else: 

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request,'An account for ' + user + ' was successfully created')


            return redirect('updateprofile')


    context = {'form': form}
    return render (request, 'registration/signup.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
    

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
