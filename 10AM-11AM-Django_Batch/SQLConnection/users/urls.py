from django.urls import path
from . import views

urlpatterns = [
    path("",views.for_user),
    path("register/",views.registration)
    
]
