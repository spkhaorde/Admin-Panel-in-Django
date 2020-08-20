from django import forms
from .models import Task
from django.contrib.auth.models import User
#from s3direct.widgets import S3DirectWidget

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = User
		#fields = '__all__'
		fields = ('username','first_name','last_name','email','password')

	def __init__(self,*args,**kwargs):
		super(EmployeeForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True
		#self.fields['username'].widget.attrs['readonly'] = True

class TaskForm(forms.ModelForm):
	class Meta:
		#images = forms.URLField(widget=S3DirectWidget(dest='primary_destination'))
		model = Task
		#fields = ('employee_name','title','description')
		fields = '__all__'

