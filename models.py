from django.db import models
from django.contrib.auth.models import User
import os
#from s3direct.fields import S3DirectField

# Create your models here.

status =( ('completed', 'completed'),('In progress', 'In progress'),('on hold', 'on hold'))

class Task(models.Model):
	id = models.AutoField(primary_key=True)
	#employee_name = models.CharField(max_length=100)
	employee_name = models.ForeignKey(User, on_delete=models.CASCADE,to_field='username')
	title = models.CharField(default='None',blank=False,max_length=50)
	description = models.TextField(default=None)
	percentage = models.CharField(max_length=100,blank = True)
	status = models.CharField(max_length=50,choices=status,blank=True)
	queries = models.CharField(default='None',blank = True,max_length=200)
	assigned_date = models.DateField(auto_now=False, auto_now_add=True)
	attachment = models.FileField(blank=True)
	#attachment = S3DirectField(dest='primary_destination', blank=True)




