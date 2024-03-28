from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager




class God(AbstractUser):
    user_name= models.CharField(max_length=50,unique=True)
    email    = models.CharField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="god_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="god_user_set",
        related_query_name="user",
    )



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
    region                          =     models.CharField(max_length=100)
    database_code                   =     models.CharField(max_length=200)
    phn_number                      =     models.CharField()
    password                        =     models.CharField()
    logo                            =     models.ImageField(max_length=1024)
    school                          =     models.BooleanField(default = False) 
    is_block                        =     models.BooleanField(default=False)

class Subject(models.Model):
    subject                         =     models.CharField(max_length=50,null=True)
class Teacher(models.Model):
    first_name                      =     models.CharField(max_length=50)
    last_name                       =     models.CharField(max_length=50)
    email                           =     models.EmailField(unique=True,blank=True)
    phone_number                    =     models.CharField(null=True,max_length=10)
    password                        =     models.CharField(max_length=100,blank=True)
    gender                          =     models.CharField(max_length=15 ,blank= True , null = True)
    subject                         =     models.ManyToManyField(Subject,related_name='teacher_subject')

class ClassName(models.Model):
    class_name                      =     models.CharField(max_length=50 ,  null=True)
    division                        =     models.CharField(max_length=20,null=True , unique = True)
    medium                          =     models.CharField(max_length=50)
    category                        =     models.CharField(max_length=50)
    teacher                         =     models.ForeignKey(Teacher,on_delete=models.CASCADE, null=True , blank=True)
    subjects                        =     models.ManyToManyField(Subject,related_name='class_subject')
    # textbook                      =     models.ManyToManyField()
    level                           =     models.CharField()

    # publication_name              =     models.foreignkey()




class Student(models.Model):
    student_name                    =     models.CharField(max_length=50)
    roll_no                         =     models.CharField(max_length=100,unique=True)
    number                          =     models.CharField(max_length=15 ,blank= True , null = True)
    email                           =     models.EmailField(unique=True)
    gender                          =     models.CharField(max_length=15 ,blank= True , null = True)
    dob                             =     models.DateField(null = True , blank = True )
    password                        =     models.CharField(max_length = 100 , null = True , blank = True)
    subjects                        =     models.ManyToManyField(Subject,related_name='student_subject') 



