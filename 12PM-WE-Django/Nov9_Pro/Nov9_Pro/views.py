from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blogs(request):
    return render(request,"blogs.html")

def contact(request):
    return render(request,"contactus.html")


def status(request):
    return render(request,"status.html")


