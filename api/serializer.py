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
