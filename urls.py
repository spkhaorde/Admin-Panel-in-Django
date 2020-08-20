from django.contrib import admin
from django.urls import path , include
from . import views



urlpatterns = [
	path('',views.home,name='home'),
	path('login',views.login_form,name='login_form'),
	path('logout',views.logout,name = 'logout'),
	path('user_form',views.employee_form,name = 'employee_form'),
	path('task_form',views.task_form,name = 'task_form'),
	path('user_list',views.user_list,name = 'user_list'),
	path('task_list',views.task_list,name = 'task_list'),
	path('ajax/crud/update/',views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
	path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
	
    #path('admin/', admin.site.urls),
]