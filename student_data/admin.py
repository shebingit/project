import imp
from django.contrib import admin
from .models import *

admin.site.register(course_data)
admin.site.register(student_data)