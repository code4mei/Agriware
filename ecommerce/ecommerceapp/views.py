from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def prediction(request):
    return render(request,"prediction.html")

def index1(request):
    return render(request,"index1.html")

