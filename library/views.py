from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')

def profile(request):
    return render(request, 'profile.html')

def search(request):
    return render(request, 'search.html')