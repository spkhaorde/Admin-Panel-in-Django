from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import EmployeeForm , TaskForm
from .models import Task
from django.contrib.auth.models import User,auth
from django.views.generic import View
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
import os
from django.contrib import messages


# Create your views here.

def home(request):
	#work_list = Work.objects.all()
    if request.user.is_authenticated:
        request.session.set_expiry(500)
        return render(request,'index.html')
    else:
        print('user not logged in')
        return login_form(request)

def login_form(request):
    #work_list = Work.objects.all()
    if request.method =="POST":
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = auth.authenticate(username=username, password=password)
       if user is not None:
        auth.login(request,user)
        request.session.set_expiry(500)
        return render(request,'index.html')
       else:
        messages.info(request,'Invalid Credentials')
        #return redirect('/login')
        return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    print('user logged out')
    return render(request,'login.html')



def employee_form(request):
    if request.user.is_authenticated:
        if request.method =="GET":
            form = EmployeeForm()
            return render(request,'userform.html',{'form':form})
        else:
            form = EmployeeForm(request.POST)
            if form.is_valid() or True:
                form.save()
                return redirect('/')
    else:
        print('user not logged in')
        return login_form(request)

def task_form(request):
    #print(os.getcwd())
    if request.user.is_authenticated:
        subject = 'Assigned Task'
        from_email = settings.EMAIL_HOST_USER
        
        
        if request.method =='GET':
            task = Task.objects.all()
            form2 = TaskForm()
            return render(request,'task_list.html',{'work_list':task,'form':form2})
        else:
            form2 = TaskForm(request.POST)
            if form2.is_valid() or True:
                print('formfield employee',form2.cleaned_data.get("employee_name"))
                print('formfield title',form2.cleaned_data.get("title"))
                print('formfield description',form2.cleaned_data.get("description"))

                title_asignee = form2.cleaned_data.get("title")
                description_asignee = form2.cleaned_data.get("description")
                task_asignee = form2.cleaned_data.get("employee_name")
                user_asignee = User.objects.get(username = task_asignee)
                print(user_asignee.email)
                
                message = 'The Following taks is assigned to you'+'\n'+str(title_asignee)+'\n'+str(description_asignee)
                to_list = [str(user_asignee.email)]
                send_mail(subject,message,from_email,to_list,fail_silently=False,)

                form2.save()
                return redirect('/task_form')
            else:
                return home(request)
    else:
        return login_form(request)



def user_list(request):
    if request.user.is_authenticated:
        user_list = User.objects.all()
        return render(request,'user_list.html',{'user_list':user_list})
    else:
        return login_form(request)

def task_list(request):
    if request.user.is_authenticated:
        task_list = Task.objects.all()
        return render(request,'total_task_list.html',{'work_list':task_list})
    else:
        return login_form(request)

class UpdateCrudUser(View):
    def get(self, request):
        employee = request.GET.get('employee',None)
        print(employee)
        task_id = request.GET.get('taskid',None)
        print(task_id)
        title = request.GET.get('title',None)
        print(title)
        description = request.GET.get('description',None)
        print(description)
        obj = Task.objects.get(id=int(task_id))
        #obj.employee_name_id = employee
        obj.title = title
        obj.description = description
        #obj.age = age1
        obj.save()
        task = {'taskid':task_id,'employee_name_id':obj.employee_name_id,'title':obj.title,'description':obj.description}
        data = {
            'task': task
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        print('employee task to delete',id1)
        Task.objects.get(id=int(id1)).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)   



