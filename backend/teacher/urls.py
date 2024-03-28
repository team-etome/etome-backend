from django.urls import path
from django.conf import settings
from teacher import views



urlpatterns=[
    path('api/excelteacher',views.UploadExcelTeacher.as_view(),name='uploadExcelOfTeacher'),
    path('api/teacherlogin',views.TeacherLoginView.as_view(),name='teacherlogin'),
    path('api/teacherdetails',views.TeacherDetails.as_view(),name='teacherdetails'),
    path('api/teacherlogin/<int:pk>',views.TeacherLoginView.as_view(),name='teacher_one_details'),

   
   
]