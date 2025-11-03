from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("I am about page")

def home(request):
    data={
        'title':'My Nov2 Projet',
        'about':'This is Django Practice Project',
        'services':['Python','SQL','ML','DL','Django'],
        'student_details':[
            {'name':'Ramandeep','address':'Noida'},
            {'name':'Shanu Singh','address':'Delhi'},
            {'name':'Umesh Saini','address':'Noida'}
        ]
    }
    return render(request,'index.html',data)


