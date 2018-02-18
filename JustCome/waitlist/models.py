from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

#The patient model
class Patient(models.Model):
    patientID = models.TextField(max_length = 10)
    position = models.IntegerField()
    priority = models.TextField(max_length = 30)
>>>>>>> 3ee36131822d71f22557ae1b5e90438e9e40c3e9
