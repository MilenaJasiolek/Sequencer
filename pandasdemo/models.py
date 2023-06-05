from django.db import models

# Defining the models

class Student(models.Model):
    name=models.CharField(max_length=200)
    rollnum=models.IntegerField()
    rank=models.IntegerField()