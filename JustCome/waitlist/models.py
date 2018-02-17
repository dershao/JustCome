from django.db import models

# Create your models here.

#The patient model
class Patient(models.Model):
    patientID = models.CharField(max_length = 4)
    device = models.CharField(max_length = 30)
    priority = models.CharField(max_length = 30)