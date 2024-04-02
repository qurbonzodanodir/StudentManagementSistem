from django.shortcuts import render
from .serializer import *
from rest_framework import permissions
from rest_framework import generics
from .models import *



class StudentCreateApi(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializerApi
    permission_classes = (permissions.IsAdminUser,)


class StudentListApi(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializerApi
    permission_classes = (permissions.IsAdminUser,)



class StudentUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializerApi
    permission_classes = (permissions.IsAdminUser,)



class TeacherCreateApi(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializerApi
    permission_classes = (permissions.IsAdminUser,)


class TeachertUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializerApi
    permission_classes = (permissions.IsAdminUser,)



class TeacherListApi(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializerApi
    permission_classes = (permissions.AllowAny,)



class CourseCreateApi(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerApi
    permission_classes = (permissions.IsAdminUser,)


class CourseUpdateApi(generics.RetrieveUpdateDestroyAPIView,):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerApi
    permission_classes = (permissions.IsAdminUser,)


class CourseListApi(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerApi
    permission_classes = (permissions.AllowAny,)

