from django.shortcuts import render
from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")
def registration(request):
    error=""
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        #patientid=request.POST['patientid']
        address=request.POST['address']
        contactno=request.POST['contact no']
        age=request.POST['age']
        gender=request.POST['gender']
        bg=request.POST['blood group']
        uname=request.POST['emailid']
        pwd=request.POST['password']
        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=pwd)
            Patient.objects.create(user=user,gender=gender,address=address,age=age,contactno=contactno,bloodgroup=bg)
            error="no"
        except:
            error="yes"
    return render(request,"registration.html",locals())
def patlogin(request):
    if request.method=='POST':
        u=request.POST['email']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        print(user)
        if user!=None:
            pat=Patient.objects.get(user=user)
            error="no"
        else:
            error="yes"

    return render(request,"login.html",locals())
def adminlogin(request):
    error=""
    if request.method =="POST":
        u=request.POST['username']
        p=request.POST['password']
        
        user=authenticate(request,username=u,password=p)
        #print(user)
        if user:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        else:
            error="yes"
    return render(request,'adminlogin.html',locals())
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')
def patienthome(request):
    return render(request,"patienthome.html")
def adminhome(request):
    app=appointment.objects.all()
    pat=Patient.objects.all()
    doc=Doctor.objects.all()
    doccount=doc.count()
    patcount=pat.count()
    appointmentcount=appointment.objects.all().count()
    return render(request,"adminhome.html",locals())
def acceptappointment(request,appid):
    error=""
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    u=appointment.objects.get(appid=appid)
    u.status="Accepted"
    try:
        u.save()
        error="no"
    except:
        error="yes"
    return render(request,"adminhome.html",locals())




