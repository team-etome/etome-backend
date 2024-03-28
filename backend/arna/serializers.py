from rest_framework import serializers
from.models import *
class QuestionPaperSerializer(serializers.ModelSerializer):
     class Meta:
        model   =  QuestionPaper
        fields = ['id','exam_name','subject','classname','division','category','term','start_time','end_time','exam_date','teacher','total_marks','instructions']

class SeatingArrangementSerializer(serializers.ModelSerializer):
     class Meta:
        model   = SeatingArrangement
        fields = ['id','class_number','exam_date','exam_time','class_name','division','category','teacher','pattern']