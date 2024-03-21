from rest_framework import serializers
from app1.models import *
from django.contrib.auth.hashers import make_password



class GodSerializer(serializers.ModelSerializer):

    class Meta:
        model = God
        fields = ['email','password']

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['institute_name','institute_code','email_id','eduational_body','address','database_code','phn_number','password','logo']


        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.password = make_password(password)
            instance.save()
            return instance

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subject','subject_code']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields=['class_name','division','subject']

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = [ 'subjects',  'name', 'email',  'phone_number', 'password',]

    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects', [])
        password = validated_data.pop('password', None)
        teacher = Teacher(**validated_data)

        if password is not None:
            teacher.password = make_password(password)
        teacher.save()

        for subject in subjects_data:
            teacher.subjects.add(subject)

        return teacher
    


