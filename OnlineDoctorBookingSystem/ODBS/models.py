from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    docid=models.BigAutoField(primary_key=True)
    contactno=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    specialist=models.CharField(max_length=50,null=True)
    day1=models.CharField(max_length=10,null=True)
    day2=models.CharField(max_length=10,null=True)
    day3=models.CharField(max_length=10,null=True)
    time1=models.CharField(max_length=10,null=True)
    time2=models.CharField(max_length=10,null=True)
    time3=models.CharField(max_length=10,null=True)
    dept=models.CharField(max_length=10,null=True)

    def __str__(self):
        return str(self.pk)
class Patient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    patid=models.BigAutoField(primary_key=True)
    gender=models.CharField(max_length=10, default="Male")
    address=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=10,null=True)
    contactno=models.CharField(max_length=10,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    docid=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.pk)
class appointment(models.Model):
    appid=models.BigAutoField(primary_key=True)
    patid=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    docid=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    date=models.DateField(max_length=50,null=True)
    starttime=models.TimeField(max_length=50,null=True)
    status=models.CharField(max_length=50,default="Pending")
    def __str__(self):
        return str(self.pk)


