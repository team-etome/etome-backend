from django.db import models
from app1.models import *

class QuestionPaper(models.Model):
    STATUS_CHOICES = (
        ('send'  , 'send'),
        ('submitted' , 'submitted'),
        ('approved' , 'approved'),
        ('declined' , 'declined'),
    )
    exam_name        =  models.CharField(max_length = 150)
    subject          =  models.ForeignKey(Subject ,on_delete=models.CASCADE , null = True , blank = True) 
    class_name       =  models.ForeignKey(ClassName ,on_delete=models.CASCADE , null = True , blank = True)
    division         =  models.CharField(max_length = 15,null = True , blank = True)
    category         =  models.CharField(max_length = 15,null=True,blank = True)
    term             =  models.CharField(max_length = 15,null=True,blank = True)
    start_time       =  models.TimeField(blank = True , null = True)
    end_time         =  models.TimeField(blank = True , null = True)
    exam_date        =  models.DateField()
    teacher          =  models.ForeignKey(Teacher ,on_delete=models.CASCADE, blank = True , null = True)
    total_marks      =  models.IntegerField(max_length = 15,null=True,blank = True)
    instructions     =  models.ImageField()
    status           =  models.CharField(choices = STATUS_CHOICES,default='send')


class SeatingArrangement(models.Model):

    PATTERN_CHOICES = [
        ('vertical_arrangement', 'vertical_arrangement'),
        ('horizondal_arranegement', 'horizondal_arranegement')
    ]

    class_number         =  models.CharField(max_length=100)
    exam_date            =  models.DateField(null = True , blank = True)
    exam_time            =  models.CharField(null = True , blank = True)
    class_name           =  models.CharField(max_length=100,null = True , blank = True)
    division             =  models.CharField(max_length = 50, null = True , blank = True)
    category             =  models.CharField(max_length = 50, null = True , blank = True)
    teacher              =  models.ForeignKey(Teacher , on_delete = models.CASCADE ,null = True , blank = True)
    pattern              =  models.CharField(max_length=50, choices=PATTERN_CHOICES)


    

