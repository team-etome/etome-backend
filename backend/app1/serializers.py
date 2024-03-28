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
        fields = ['institute_name','institute_code','email_id','eduational_body','address','region','database_code','phn_number','password','logo']


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


class ClassNameSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    class Meta:
        model = ClassName
        fields = ['class_name', 'division', 'medium', 'category', 'teacher', 'subjects', 'level']

    def get_level(self, obj):
        class_name = obj.class_name
        if 5 <= int(class_name) <= 7:
            return "Upper Primary"
        elif 8 <= int(class_name) <= 10:
            return "Higher School"
        elif 11 <= int(class_name) <= 12:
            return "Higher Secondary"
        else:
            return "Unknown"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['level'] = self.get_level(instance)
        return data


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = [ 'subjects',  'first_name','last_name', 'email',  'phone_number', 'password',]

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
    


