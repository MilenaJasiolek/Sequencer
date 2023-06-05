from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# CRUD (Create, Read, Update, Delete) operations for the Student
# Register the Student model with the admin site
admin.site.register(Student)

