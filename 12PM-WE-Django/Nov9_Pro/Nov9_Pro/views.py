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

def addition(request):
    return render(request,'addition.html')

def add(request):
    n1 = float( request.GET.get('n1') )
    n2 = float( request.GET.get('n2') )
    n3 = n1+n2
    return render(request,'addition.html',{'output':n3})