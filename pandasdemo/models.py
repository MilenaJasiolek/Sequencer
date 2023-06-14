from django.db import models

# Defining the models
class Sequencer(models.Model):
    species=models.CharField(max_length=20)
    sequence=models.CharField(max_length=500)
    name=models.CharField(max_length=50)