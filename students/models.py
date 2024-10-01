from django.db import models

from django.db import models

class Student(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    lname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    bday = models.DateField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    entrydate = models.DateField()
    actgrade = models.IntegerField
    