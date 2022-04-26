from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/pages/home.html')

def login(request):
    return render(request, 'app/pages/login.html')

def register(request):
    return render(request, 'app/pages/register.html')

def feed(request):
    return render(request, 'app/pages/feed.html')
