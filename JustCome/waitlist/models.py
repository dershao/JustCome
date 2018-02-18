from django.db import models

# Create your models here.

#The patient model
class Patient(models.Model):
    patientID = models.TextField(max_length = 10)
    position = models.IntegerField()
    priority = models.TextField(max_length = 30)