from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'home'
    }
    return render(request,'home/home.html', context,)

def landing(request):
    return render(request, 'home/landing.html')

def base(request):
    return render(request, 'home/base.html')

def about(request):
    return render(request,'home/about.html')