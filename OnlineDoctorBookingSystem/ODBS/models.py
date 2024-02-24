from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    docid=models.BigAutoField(primary_key=True)
    contactno=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    specialist=models.CharField(max_length=50,null=True)
class Patient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    patid=models.BigAutoField(primary_key=True)
    gender=models.CharField(max_length=10, default="Male")
    address=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=10,null=True)
    contactno=models.CharField(max_length=10,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    docid=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    
