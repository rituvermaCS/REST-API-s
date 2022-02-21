from django.db import models

# Create your models here.

class Task(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_sn = models.IntegerField(max_length=10)
    email = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    objects = models.Manager() 
   
