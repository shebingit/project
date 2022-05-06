
from django.db import models
from django.contrib.auth.models import User

#creating course table

class course_data(models.Model):

    cu_name=models.CharField(max_length=20)
    cu_fee=models.IntegerField()

def __str__(self):
        return self.cu_name

#creating student table

class student_data(models.Model):
    course_data=models.ForeignKey(course_data,on_delete=models.CASCADE, null=True,blank=True)
    st_name=models.CharField(max_length=25)
    st_address=models.CharField(max_length=30)
    st_age=models.IntegerField()
    st_dob=models.CharField(max_length=30)

def __str__(self):
        return self.course_data

