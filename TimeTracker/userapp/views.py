from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import CreateView
from django.contrib import messages
from userapp.models import Register,Task
def saveregister(request):
    if request.method == "POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        uname=request.POST.get("username")
        pword=request.POST.get("password")
        cpword=request.POST.get("cpassword")
        if pword != cpword:
            messages.success(request,"Both Passwords Must Be Same")
        else:
            Register(firstname=fname,lastname=lname,username=uname,password=pword,confirm_password=cpword).save()
            messages.success(request,"Successfuly Registered")
            return render(request,'userpages/register.html')
        return render(request,"userpages/register.html",)
def loginvalidation(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        request.session["uname"] = uname
        pword=request.POST.get('password')
        qs=Register.objects.filter(username=uname,password=pword)
        if qs:
            return redirect('/user/tasksave/')

        else:
            messages.success(request,"Please Enter Valid Details")
            return render(request, 'userpages/login.html')
def tasksave(request):
    if request.method =='POST':
        taskhead=request.POST.get('taskhead')
        taskdesc=request.POST.get('taskdesc')
        print(taskdesc,'$'*15)
        date=request.POST.get('date')
        username = request.session['uname']
        print(username)

        Task(taskhead=taskhead,taskdesc=taskdesc,task_date=date,username=username).save()
    username = request.session['uname']
    data=Task.objects.filter(username=username)
    data1=Register.objects.filter(username=username)
    return render(request,'userpages/welcome.html',{"data":data,'data1':data1})

def logout(request):
    del request.session['uname']
    return HttpResponse("<strong>You are logged out.</strong>")

from datetime import datetime
def closetime(request):
    task_id=request.GET.get('idno')
    import datetime
    a = datetime.datetime.now()
    tt = a.strftime('%H:%M:%S.%f')
    print(tt)
    Task.objects.filter(task_id=task_id).update(closetime=tt)
    return redirect('/user/tasksave/')