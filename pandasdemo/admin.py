from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

#register model
admin.site.register(Student)

