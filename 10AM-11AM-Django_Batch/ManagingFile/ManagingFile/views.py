from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse("Hello, Django!")

def home(request):
    data = {
        'name': 'Raman Singh',
        'address': 'Delhi',
        'age': 24,
        'is_login': True,
        'city': ['Delhi', 'Noida', 'Gurgaon', 'Faridabad']
    }
    return render(request, 'index.html',data)