from django.db import models

# Create your models here.
class Register(models.Model):

    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    starttime=models.TimeField(auto_now_add=True)
    username=models.EmailField(primary_key=True,max_length=30)
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
class Task(models.Model):
    username=models.EmailField(max_length=30)
    task_date = models.DateField(auto_now_add=True)
    task_id=models.AutoField(primary_key=True)
    starttime=models.TimeField(auto_now_add=True)
    taskhead = models.CharField(max_length=50)
    taskdesc = models.TextField(max_length=100)
    closetime=models.TimeField(auto_now_add=True)

