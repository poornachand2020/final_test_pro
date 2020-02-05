"""TimeTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from TimeTracker import settings
from django.views.generic import TemplateView,CreateView
from django.conf.urls.static import static
from userapp import views
from userapp.models import Register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',TemplateView.as_view(template_name="userpages/homepage.html")),
    path('register/',TemplateView.as_view(template_name='userpages/register.html')),
    path('save/',views.saveregister),
    path('login/',TemplateView.as_view(template_name='userpages/login.html')),
    path('loginvalidation/',views.loginvalidation),
    path('tasksave/',views.tasksave),
    path('logout/',views.logout),
    path('closetime/',views.closetime)
    #path('taskshow/',views.taskshow),




]

