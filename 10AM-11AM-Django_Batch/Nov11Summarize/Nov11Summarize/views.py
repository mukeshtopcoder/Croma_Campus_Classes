from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def status(request):
    return render(request,'addition.html')
def blogs(request):
    return render(request,'blogs.html')
def contact(request):
    return render(request,'contact.html')

def addition(request):
    try:
        num1 = float(request.GET.get("n1"))
        num2 = float(request.GET.get("n2"))
    except:
        num1 = num2 = 0
    num3 = num1+num2
    result = str(num1)+" + "+str(num2)+" = "+str(num3)
    return render(request,'addition.html',{'output':result})