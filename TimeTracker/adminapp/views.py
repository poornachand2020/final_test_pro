from django.shortcuts import render,redirect,HttpResponse
from .models import Admin
from django.contrib import messages

from userapp.models import Register,Task

# Create your views here.
def adminlogin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        request.session["uname"] = uname
        pword=request.POST.get('password')
        qs=Admin.objects.filter(username=uname,password=pword)
        if qs:
            return redirect('/adminpage/adminhome/')

        else:
            messages.success(request,"Please Enter Valid Details")
            return render(request, 'userpages/login.html')


def usersdetails(request):
    qs=Register.objects.all()

    if qs:
        return  render(request,'adminpages/userdetails.html/',{'data': qs})

    return None


def usersdetails1(request):
    username=request.GET.get('idno')
    print(username,'*'*15)
    qs=Task.objects.filter(username=username)
    if qs:
        return  render(request,'adminpages/userdetails_show.html',{'data':qs})
    else:
        return HttpResponse('Not Valid')

