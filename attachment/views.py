from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import *
from datetime import datetime

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            supervisor=Supervisor.objects.get(supervisor=User(id=request.user.id))
            student=Student.objects.filter(department=supervisor.department)
            stu=User.objects.all()
            context={
               'supervisor':supervisor,
               'student':student,
               'stu':stu,
            }
            return render(request, 'admin.html', context)
        else:
            student=Student.objects.get(username=request.user.username)
            logs=Logs.objects.filter(student=request.user.id)
            context={
                'student':student,
                'logs':logs,
            }
            return render(request, 'my.html', context)
    else:
        return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pwd']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        return redirect('/my')
    return render(request, 'login.html')

def signup(request):
    i=Institution.objects.all()
    d=Department.objects.all()
    context={
        'institution':i,
        'department':d,
    }
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        idnum=request.POST['idnum']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['pwd']
        password2=request.POST['pwd2']
        institution=request.POST['institution']
        refcode=request.POST['ref']
        phone=request.POST['phone']
        department=request.POST['department']
        startdate=datetime.strptime(request.POST['sdate'], "%Y-%m-%d")
        enddate=datetime.strptime(request.POST['edate'], "%Y-%m-%d")
        if password == password2:
            if User.objects.filter(username=idnum).exists():
                messages.info(request,'User already exist')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=fname, last_name=lname,username=idnum, email=email, password=password)
                user.save()
                val=Student.objects.create(username=idnum,institution=Institution(id=institution),department=Department(id=department),refcode=refcode,phone=phone,startdate=startdate,enddate=enddate)
                val.save()
                return redirect('login')
        else:
            messages.info(request,'Password not same')
            return redirect('signup')
    else:
        if request.user.is_authenticated:
            return redirect('/my')
        else:
            return render(request, 'signup.html', context) 
        

def logout(request):
    auth.logout(request)
    return redirect('login')

def logs(request):
    if request.method=='POST':
        rid=request.user.id
        startdate=datetime.strptime(request.POST['wstart'], "%Y-%m-%d")
        enddate=datetime.strptime(request.POST['wend'], "%Y-%m-%d")
        activityDone=request.POST['activity']
        newSkillsAquired=request.POST['skills']
        challangesMet=request.POST['challanges']
        OtherCommenjts=request.POST['comment']
        log=Logs.objects.create(student=User(id=rid), startdate=startdate,enddate=enddate, activityDone=activityDone, newSkillsAquired=newSkillsAquired, challangesMet=challangesMet )
        log.save()
        return redirect('/my')
        
def studentlog(request, id):
    user=User.objects.get(id=id)
    logs=Logs.objects.filter(student=request.user.id)
    context={
     "user":user,  
     "logs":logs,
    }
    return render(request, 'view.html', context)
    
    
    
