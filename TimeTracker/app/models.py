# import datetime
#
# from django.db import models
#
# # Create your models here.
#
# class Rigister:
#     firstname=models.CharField(max_length=30)
#     lastname=models.CharField(max_length=30)
#     date=models.DateTimeField(auto_now_add=True)
#     starttime=models.TimeField(auto_now_add=True)
#     username=models.EmailField(primary_key=True,max_length=30)
#     password=models.CharField(max_length=30)
#     confirm_password=models.CharField(max_length=30)
#
#
# class User:
#     username=models.EmailField(primary_key=True,max_length=30)
#     password=models.CharField(max_length=30)
#
#
# class Task:
#     user=models.ForeignKey(on_delete=models.CASCADE)
#     task_id=models.AutoField()
#     starttime=models.TimeField(auto_now_add=True)
#     taskhead = models.CharField(max_length=50)
#     taskdesc = models.TextField(max_length=100)
#     closetime=models.TimeField(default=None)
#
