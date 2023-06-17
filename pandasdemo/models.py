from django.db import models

# Defining the models
class Sequencer(models.Model):

    # defining the species
    species=models.CharField(max_length=20)
    # defining the sequences
    sequence=models.CharField(max_length=500)
    # defining the name of organism
    name=models.CharField(max_length=50)