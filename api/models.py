from django.db import models


class Students(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
  
    f_name = models.CharField(max_length=80)
    l_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=120)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=5,choices = GENDER_CHOICES)


    def __str__(self):
        return f"{self.f_name}  {self.l_name}  "



class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    f_name = models.CharField(max_length=80)
    l_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length = 100)
    gender = models.CharField(max_length = 5,choices = GENDER_CHOICES)
    address = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.f_name}  {self.l_name}  "




class Course(models.Model):
    title = models.CharField(max_length = 80)
    descriptioin = models.TextField()
    duration = models.DateField()
    cost = models.IntegerField()
    students = models.ManyToManyField(Students,related_name='students')
    teacher = models.ManyToManyField(Teacher,related_name='teacher')


    def __str__(self):
        return self.title
    







