from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import  ProfileForm, BookForm,  CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import json
from django.views.generic.edit import UpdateView



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
    wishlist, created = Wishlist.objects.get_or_create(user=current_user.profile)
    wishitems = wishlist.wishlistitem_set.all()
        
    return render(request, 'profile.html', {"current_user":current_user,"books":books,"wishitems":wishitems, "profiles":profiles})

@login_required(login_url='login')
def swap(request):
    current_user = request.user
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    books =Book.objects.filter(user_id = current_user.id).all()
    swap, created = Swap.objects.get_or_create(user=current_user.profile)
    items = swap.swapitem_set.all()


    return render(request, 'swap.html', {"current_user":current_user,"items":items,"books":books, swap:swap, "profiles":profiles, items:items})
    
def updateSwap(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']
    profile = request.user.profile
    book = Book.objects.get(id=bookId)

    swap, created = Swap.objects.get_or_create(user=profile)

    swapItem, created =SwapItem.objects.get_or_create(swap=swap, book=book)

    if action == 'add':
        swapItem = (swapItem.quantity + 1)
         
    elif action == 'remove':
        swapItem.quantity = (swapItem.quantity - 1)

        swapItem.save()

        if swapItem.quantity <= 0:
            swapItem.delete()

    return JsonResponse('Item was added', safe=False)

def updateItem(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']
    profile = request.user.profile
    book = Book.objects.get(id=bookId)


    wishlist, created = Wishlist.objects.get_or_create(user=profile)

    wishlistItem, created = WishlistItem.objects.get_or_create(wishlist=wishlist, book=book)

    if action == 'add':
        wishlistItem = (wishlistItem.quantity + 1)   
        
    elif action == 'remove':
        wishlistItem.quantity = (wishlistItem.quantity - 1)
        
        wishlistItem.save()
        
        if wishlistItem.quantity <= 0:
            wishlistItem.delete()


    return JsonResponse('Item was added', safe=False)



class search(ListView):

    model = Book
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(synopsis__icontains=query) | Q(user__username__icontains=query) | Q(location__icontains=query) 
        )

        return object_list

    

@login_required(login_url='login')
def updateprofile(request):
    current_user = request.user
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    books =Book.objects.filter(user_id = current_user.id).all()
    wishlist, created = Wishlist.objects.get_or_create(user=current_user.profile)
    wishitems = wishlist.wishlistitem_set.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'updateprofile.html', {"current_user":current_user,"books":books,"wishitems":wishitems, "profiles":profiles, 'form':form})

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

        form = CreateUserForm(request.POST)

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request,'An account for ' + user + ' was successfully created')

                return redirect('login')

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



