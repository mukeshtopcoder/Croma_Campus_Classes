from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request,'index.html',{'title':'My New Project'})

def show_students(request):
    students = Student.objects.all()
    data = " , ".join([str(student.name) for student in students])
    return render(request,'students.html',{'students':data})