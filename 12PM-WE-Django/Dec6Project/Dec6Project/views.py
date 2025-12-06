from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def newpage(request):
    return render(request,'nextpage.html')

