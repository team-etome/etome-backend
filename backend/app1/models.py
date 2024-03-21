from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager




class God(AbstractUser):
    user_name= models.CharField(max_length=50,unique=True)
    email    = models.CharField(unique=True)



    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email


class Admin(models.Model):
    institute_name                  =     models.CharField(max_length=200)
    institute_code                  =     models.CharField(max_length=200,unique=True)
    email_id                        =     models.EmailField(unique=True )
    eduational_body                 =     models.CharField(max_length=200)
    address                         =     models.CharField(max_length=200)
    database_code                   =     models.CharField(max_length=200)
    phn_number                      =     models.CharField()
    password                        =     models.CharField()
    logo                            =     models.ImageField(max_length=1024)
    school                          =     models.BooleanField(default = False) 


class ClassName(models.Model):
    class_name                      =     models.CharField(max_length=50 ,  null=True)
    division                        =     models.CharField(max_length=20,null=True , unique = True)
  

class Subject(models.Model):
    subject                         =     models.CharField(max_length=50,null=True)
    className                       =     models.ForeignKey(ClassName, on_delete=models.CASCADE , null=True , blank=True)



class Teacher(models.Model):
    subject                         =     models.ManyToManyField(Subject)
    name                            =     models.CharField(max_length=50)
    email                           =     models.EmailField(unique=True,blank=True)
    phone_number                    =     models.CharField(null=True,max_length=10)
    password                        =     models.CharField(max_length=100,blank=True)

class Student(models.Model):
    subjects                        =     models.ManyToManyField(Subject, blank=True) 
    student_name                    =     models.CharField(max_length=50)
    roll_no                         =     models.CharField(max_length=100,unique=True)
    number                          =     models.CharField(max_length=15 ,blank= True , null = True)
    email                           =     models.EmailField(unique=True)
    gender                          =     models.CharField(max_length=15 ,blank= True , null = True)
    dob                             =     models.DateField(null = True , blank = True )
    password                        =     models.CharField(max_length = 100 , null = True , blank = True)


