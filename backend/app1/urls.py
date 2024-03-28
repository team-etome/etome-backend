from django.urls import path
from django.conf import settings
from app1 import views


urlpatterns=[
     path ('api/adminLogin',views.AdminLoginView.as_view(),name='adminlogin'),
     path ('api/godLogin',views.GodLoginView.as_view(),name='godlogin'),
     path ('api/addadmin',views.AddAdmin.as_view() , name='addadmin'),
     path('api/addClassname',views.AddClassName.as_view(),name='addclassname'),
     path ('api/adminLogin/<int:pk>',views.AdminLoginView.as_view(),name='admin_view'),
     path ('api/adminLogin',views.AdminLoginView.as_view(),name='adminlogin'),
     path ('api/classnamedetails/<int:pk>',views.ClassNameDetailsView.as_view(),name='class_details'),


     
     ]
