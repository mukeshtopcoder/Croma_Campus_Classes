from django.http import HttpResponse    
from django.shortcuts    import render

def aboutus(request):
    return HttpResponse("I am About us Page")
def services(request):
    return HttpResponse("""
<h1>My New Project</h1>
<ul>
    <li>Bulk SMS</li>                        
    <li>Digital Marketing</li>                        
    <li>App Development</li>                        
    <li>Game Development</li>                        
</ul>
""")
def myservices(request,serviceid):
    return HttpResponse("Your Service ID is : "+str(serviceid))

def homepage(request):
    mydata = {'title':'Home Page','company':'Croma Campus',
              'services':['Django Development','Data Analytics','Data Science'],
'details' : [
        {'name':'Raman Yadav','address':'Noida'},
        {'name':'Mohan Das','address':'Delhi'},
        {'name':'Yogesh Saini','address':'Gurugram'},
        {'name':'Shiva Yadav','address':'Noida'},
        {'name':'Abishesk CHauhan','address':'Noida'},
        {'name':'Vikas Singh','address':'GZB'}
    ]
              }
    return render(request,'index.html',mydata)