from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)

class Employee(models.Model):
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    
