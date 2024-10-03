from django.db import models

class Student(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    lname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    bday = models.DateField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    ins_email = models.EmailField() 
    entry_date = models.DateField()
    actual_grade = models.ForeignKey("Grade", on_delete=models)
    
    def __str__(self):
        return f'{self.name} {self.lname} {self.bday}'
    
class Grade(models.Model):
    grade = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)