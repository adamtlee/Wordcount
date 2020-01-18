from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'message':'Welcome to the home page'})

def count(request):
    return render(request, 'count.html')

def about(request):
    return render(request, 'about.html')