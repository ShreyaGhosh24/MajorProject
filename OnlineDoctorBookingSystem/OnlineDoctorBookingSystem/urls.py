"""OnlineDoctorBookingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ODBS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('registration/', registration,name="registration"),
    path('patlogin/', patlogin,name="patlogin"),
    path('adminlogin/', adminlogin,name="adminlogin"),
    path('adminlogout/', adminlogout,name="adminlogout"),
    path('adminhome/', adminhome,name="adminhome"),
    path('patienthome/', patienthome,name="patienthome"),
    path('acceptappointment/<int:appid>', acceptappointment,name="acceptappointment"),
    path('rejectappointment/<int:appid>', rejectappointment,name="rejectappointment"),
    path('commonregistration/', commonregistration,name="commonregistration"),
    path('bookappointment/', bookappointment,name="bookappointment"),
    path('bookdoc/<int:docid>', bookdoc,name="bookdoc"),
    path('adddoctor/', adddoctor,name="adddoctor"),
    path('viewalldoctor/', viewalldoctor,name="viewalldoctor"),
    path('doclogin/', doclogin,name="doclogin"),
    path('doctorhome/', doctorhome,name="doctorhome"),
    path('doclogout/', doclogout,name="doclogout"),
    path('patlogout/', patlogout,name="patlogout"),
    #path('makeappointmenthome/', commonregistration,name="makeappointment"),
    path('docviewappointment/<int:docid>', docviewappointment,name="docviewappointment"),
    path('patviewappointment/<int:patid>', patviewappointment,name="patviewappointment"),
    path('deletedoc/<int:docid>', deletedoc,name="deletedoc"),
    path('editpatientprofile/', editpatientprofile,name="editpatientprofile"),
    path('bookinghistory/', bookinghistory,name="bookinghistory"),
    path('editdoctorprofile/', editdoctorprofile,name="editdoctorprofile"),
    path('changepassword/', changepassword,name="changepassword"),



]
