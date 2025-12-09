from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def for_user(request):
    return HttpResponse("All users are here!")

def registration(request):
    return render(request,"index.html")