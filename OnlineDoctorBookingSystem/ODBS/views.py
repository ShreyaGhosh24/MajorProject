from django.shortcuts import render
from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from datetime import *

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
    if not request.user.is_authenticated:
        return redirect('commonregistration')
    user=request.user
    print(user)
    user=request.user
    pat=Patient.objects.get(user=user)
    return render(request,"patienthome.html",locals())
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
def rejectappointment(request,appid):
    error=""
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    u=appointment.objects.get(appid=appid)
    
    try:
        u.delete()
        
        error="no"
    except:
        error="yes"
    return render(request,"adminhome.html",locals())
def commonregistration(request):
    errorinsignup=""
    errorinlogin=""
    if request.method=='POST':
        #choice=request.POST['slide']
        #print(choice)
        if "signup" in request.POST:
            uname=request.POST['emailid']
            pwd=request.POST['password']
            #print(uname)
            try:
                user=User.objects.create_user(username=uname,password=pwd)
                Patient.objects.create(user=user)
                errorinsignup="no"
                print(errorinsignup)
            except:
                errorinsignup="yes"
        if "login" in request.POST:
            u=request.POST['email']
            p=request.POST['password']
            u=authenticate(request,username=u,password=p)
            #print(u)
            try:
                if u!=None:
                    pat=Patient.objects.get(user=u)
                    login(request,u)
                    errorinlogin="no"
                    #return render(request,"patienthome.html")
                else:
                    errorinlogin="incorrect password"
            except:
                errorinlogin="yes"


    return render(request,"commonsignup.html",locals())
def bookappointment(request):
    listofdoctors=Doctor.objects.all()
    return render(request,"bookappointment.html",locals())
def bookdoc(request,docid):
    p=request.user
    dayofweek={0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday",6:"sunday"}
    doc=Doctor.objects.get(docid=docid)
    patientobj=(Patient.objects.get(user=p))
    p=request.user
    d={}
    slots=[]
    slot1=[]
    slot2=[]
    slot3=[]
    appday=[]
    appday.append(doc.day1)
    t1ofdoc=(datetime.strptime(doc.time1, '%H:%M'))
    t1endofdoc=datetime.strptime((t1ofdoc+ timedelta(hours=2)).strftime('%H:%M'),'%H:%M')
            #print(t1ofdoc)
            #print(t1endofdoc)
            #print(type(t1ofdoc),type(t1endofdoc))
    t=t1ofdoc
    #slot1.append(t.strftime('%H:%M'))
    for i in range(8):
        slot1.append(t.strftime('%H:%M'))
        t=t+timedelta(minutes=15)
        
    d[doc.day1]=slot1
    if doc.day2:
        if doc.time2:
            t2ofdoc=(datetime.strptime(doc.time2, '%H:%M'))
            t2endofdoc=datetime.strptime((t2ofdoc+ timedelta(hours=2)).strftime('%H:%M'),'%H:%M')
            #print(t1ofdoc)
            #print(t1endofdoc)
            #print(type(t1ofdoc),type(t1endofdoc))
            t=t2ofdoc
            slot2.append(t.strftime('%H:%M'))
            for i in range(7):
                t=t+timedelta(minutes=15)
                slot2.append(t.strftime('%H:%M'))

            appday.append(doc.day2)
            d[doc.day2]=slot2
    if doc.day3:
        if doc.time3:
            t3ofdoc=(datetime.strptime(doc.time3, '%H:%M'))
            t3endofdoc=datetime.strptime((t3ofdoc+ timedelta(hours=2)).strftime('%H:%M'),'%H:%M')
            #print(t1ofdoc)
            #print(t1endofdoc)
            #print(type(t1ofdoc),type(t1endofdoc))
            t=t3ofdoc
            slot3.append(t.strftime('%H:%M'))
            for i in range(7):
                t=t+timedelta(minutes=15)
                slot3.append(t.strftime('%H:%M'))

            appday.append(doc.day3)
            d[doc.day3]=slot3
    msg=""
    if request.method =="POST":
        dr=request.POST['reqdate']
        tr=request.POST['reqtime']
        dro=datetime.strptime(dr, '%Y-%m-%d').date()
        tro=datetime.strptime(tr, '%H:%M')
        requestedweekday=dayofweek[dro.weekday()]
        dt=doc.day1.lower()
        #print(type(dt))
        #print(requestedweekday)
        if datetime.strptime(dr, '%Y-%m-%d')<datetime.now():
            msg="Please select a future date and time"
        elif requestedweekday==doc.day1.lower():
            #t1ofdoc=(datetime.strptime(doc.time1, '%H:%M'))
            #t1endofdoc=datetime.strptime((t1ofdoc+ timedelta(hours=2)).strftime('%H:%M'),'%H:%M')
            #print(t1ofdoc)
            #print(t1endofdoc)
            #print(type(t1ofdoc),type(t1endofdoc))
            #t=t1ofdoc
            #slot1.append(t.strftime('%H:%M'))
            #for i in range(7):
                #t=t+timedelta(minutes=15)
                #slot1.append(t.strftime('%H:%M'))
            
            if tro>=t1ofdoc and tro<t1endofdoc:
                print(tr,slot1)
                if tr in slot1:
                    objexist=appointment.objects.filter(docid=docid,date=dr,starttime=tr)
                    if not objexist:
                    #print("appointment can be scheduled")
                        try:
                            appobject=appointment.objects.create(docid=doc,patid=patientobj,date=dr,starttime=tr,status="Accepted")
                            appobject.save()
                            msg="Appointment successful!"
                        except:
                            msg="something went wrong"
                        

                    else:
                        msg="Already has an appointment"
                else:
                    msg="Please select a right slot"

            else:
                msg="Please select a right time"

        elif doc.day2 and requestedweekday==doc.day2.lower():
            t2ofdoc=(datetime.strptime(doc.time2, '%H:%M'))
            t2endofdoc=datetime.strptime((t2ofdoc+ timedelta(hours=2)).strftime('%H:%M'),'%H:%M')
            #print(t1ofdoc)
            #print(t1endofdoc)
            #print(type(t1ofdoc),type(t1endofdoc))
            t=t2ofdoc
            slot2.append(t.strftime('%H:%M'))
            for i in range(7):
                t=t+timedelta(minutes=15)
                slot2.append(t.strftime('%H:%M'))
            
            if tro>=t2ofdoc and tro<t2endofdoc:
                print(tr,slot2)
                if tr in slot2:
                    objexist=appointment.objects.filter(docid=docid,date=dr,starttime=tr)
                    if not objexist:
                    #print("appointment can be scheduled")
                        try:
                            appobject=appointment.objects.create(docid=doc,patid=patientobj,date=dr,starttime=tr,status="Accepted")
                            appobject.save()
                            msg="Appointment successful!"
                        except:
                            msg="something went wrong"
                        

                    else:
                        msg="Already has an appointment"
                else:
                    msg="Please select a right slot"

            else:
                msg="Please select a right time"

        elif doc.day3 and requestedweekday==doc.day3.lower():
            t3ofdoc=(datetime.strptime(doc.time3, '%H:%M'))
            t3endofdoc=datetime.strptime((t3ofdoc+ timedelta(hours=2)).strftime('%H:%M'),'%H:%M')
            #print(t1ofdoc)
            #print(t1endofdoc)
            #print(type(t1ofdoc),type(t1endofdoc))
            t=t3ofdoc
            slot3.append(t.strftime('%H:%M'))
            for i in range(7):
                t=t+timedelta(minutes=15)
                slot3.append(t.strftime('%H:%M'))
            
            if tro>=t3ofdoc and tro<t3endofdoc:
                print(tr,slot3)
                if tr in slot3:
                    objexist=appointment.objects.filter(docid=docid,date=dr,starttime=tr)
                    if not objexist:
                    #print("appointment can be scheduled")
                        try:
                            appobject=appointment.objects.create(docid=doc,patid=patientobj,date=dr,starttime=tr,status="Accepted")
                            appobject.save()
                            msg="Appointment successful!"
                        except:
                            msg="something went wrong"
                        

                    else:
                        msg="Already has an appointment"
                else:
                    msg="Please select a right slot"

            else:
                msg="Please select a right time"

        else:
            msg="Please select a valid date or a day matched with doctor's day"
        
        
    return render(request,"bookingpage.html",locals())
def adddoctor(request):
    error=""
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['emailid']
        pwd=request.POST['password']
        phno=request.POST['phno']
        qualification=request.POST['qualification']
        spl=request.POST['spl']
        dept=request.POST['dept']
        vdate1=request.POST['vdate1']
        vdate2=request.POST['vdate2']
        vdate3=request.POST['vdate3']
        vtime1=request.POST['vtime1']
        vtime2=request.POST['vtime2']
        vtime3=request.POST['vtime3']
        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=email,password=pwd)
            Doctor.objects.create(user=user,contactno=phno,qualification=qualification,specialist=spl,dept=dept,day1=vdate1,day2=vdate2,day3=vdate3,time1=vtime1,time2=vtime2,time3=vtime3)
            error="no"
        except:
            error="yes"
    return render(request,"adddoctor.html")
def viewalldoctor(request):
    alldoc=Doctor.objects.all()
    return render(request,"viewalldoctor.html",locals())
def doclogin(request):
    if request.method=='POST':
        u=request.POST['email']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        print(user)
        try:
            if user!=None:
                doc=Doctor.objects.get(user=user)
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="Something went wrong"
        print(error)

    return render(request,"login.html",locals())
def doctorhome(request):
    if not request.user.is_authenticated:
        return redirect('doclogin')
    user=request.user
    print(user)
    user=request.user
    doc=Doctor.objects.get(user=user)
    return render(request,"doctorhome.html",locals())
def doclogout(request):
    logout(request)
    return redirect('doclogin')
def patlogout(request):
    logout(request)
    return redirect('commonregistration')
def docviewappointment(request,docid):
    user=request.user
    doc=Doctor.objects.get(docid=docid)
    appointmentsofdoc=appointment.objects.filter(docid=docid)
    return render(request,'docviewappointment.html',locals())
def patviewappointment(request,patid):
    user=request.user
    pat=Patient.objects.get(patid=patid)
    appointmentsofpat=appointment.objects.filter(patid=patid)
    return render(request,'patviewappointment.html',locals())
def deletedoc(request,docid):
    error=""
    doc=Doctor.objects.get(docid=docid)
    try:
        doc.delete()
        error="no"
        alldoc=Doctor.objects.all()
        return render(request,'viewalldoctor.html',locals())
    except:
        error="yes"
def editpatientprofile(request):
    if not request.user.is_authenticated:
        return redirect('patlogin')
    error=""
    user=request.user
    pat=Patient.objects.get(user=user)
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        #patientid=request.POST['patientid']
        address=request.POST['address']
        contactno=request.POST['contactno']
        age=request.POST['age']
        gender=request.POST['gender']
        bg=request.POST['bg']

        pat.user.first_name=fname
        pat.user.last_name=lname
        pat.address=address
        pat.contactno=contactno
        pat.age=age
        pat.gender=gender
        pat.bloodgroup=bg
        try:
            pat.save()
            pat.user.save()
            error="no"
        except:
            error="yes"
    
    return render(request,"editpatientprofile.html",locals())
def bookinghistory(request):
    user=request.user
    pid=Patient.objects.get(user=user).patid
    app=appointment.objects.filter(patid=pid)
    return render(request,"bookinghistory.html",locals())
def editdoctorprofile(request):
    if not request.user.is_authenticated:
        return redirect('doclogin')
    error=""
    user=request.user
    doc=Doctor.objects.get(user=user)
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        
        contactno=request.POST['contactno']
        qualification=request.POST['qualification']
        specialization=request.POST['specialization']
        dept=request.POST['dept']

        doc.user.first_name=fname
        doc.user.last_name=lname
        doc.contactno=contactno
        doc.specialist=specialization
        doc.qualification=qualification
        doc.dept=dept
        
        try:
            doc.save()
            doc.user.save()
            error="no"
        except:
            error="yes"
    
    
    
    return render(request,"editdoctorprofile.html",locals())
def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('doclogin')
    error=""
    user=request.user
    if request.method=='POST':
        current=request.POST['currentpassword']
        npassword=request.POST['newpassword']
        try:
            if user.check_password(current):
                user.set_password(npassword)
                user.save()
                error="no"
            else:
                error="wrongpassword"
        except:
            error="yes"

    return render(request,"changepassword.html",locals())












