from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.EmailField(primary_key=True, max_length=30)
    password=models.CharField(max_length=30)