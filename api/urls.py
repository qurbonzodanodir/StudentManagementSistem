from django.urls import path
from .views import *


urlpatterns = [
    path('create-student',StudentCreateApi.as_view()),
    path('create-teacher',TeacherCreateApi.as_view()), 
    path('create-course',CourseCreateApi.as_view()),
    path('update-student/<int:pk>',StudentUpdateApi.as_view()),
    path('update-teacher/<int:pk>',TeachertUpdateApi.as_view()),
    path('update-course/<int:pk>',CourseUpdateApi.as_view()),
    path('delete-student/<int:pk>',StudentUpdateApi.as_view()),
    path('delete-teacher/<int:pk>',TeachertUpdateApi.as_view()),
    path('delete-course/<int:pk>',CourseUpdateApi.as_view()),
    path('list-student/',StudentListApi.as_view()),
    path('list-teacher/',TeacherListApi.as_view()),
    path('list-course/',CourseListApi.as_view()),
   
]
