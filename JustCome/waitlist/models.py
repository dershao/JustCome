from django.db import models

# Create your models here.

#The patient model
class Patient(models.Model):
    patientID = models.TextField(max_length = 10)
    phoneNumber = models.TextField(max_length = 12)
    priority = models.TextField(max_length = 30)
    index = models.PositiveIntegerField();
    #Rename the default model manager from object
    Manager = models.Manager()
