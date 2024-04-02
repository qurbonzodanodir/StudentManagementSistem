from rest_framework import serializers
from .models import *

class StudentsSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class TeacherSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'  


class CourseSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class CourseListSerializerApi(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    teacher = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = ['title', 'descriptioin', 'duration', 'cost', 'students','teacher']        