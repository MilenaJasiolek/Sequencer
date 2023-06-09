from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# CRUD (Create, Read, Update, Delete) operations for the Sequencer
# Register the Sequencer model with the admin site
admin.site.register(Sequencer)

