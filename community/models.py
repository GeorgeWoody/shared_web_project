### MODELS OF THE SCHOOL COMMUNITY
### STUDENT                 (must be attached to "legal guardian" in some way)
### LEGAL GUARDIAN          (must be attached to "student" in some way)
### TEACHER                 (must be attached to "grades" in some way)
### GRADE                   (must be attached to a group of "students" in some way)
### OTHER PERSONNEL

from django.db import models

###packages###
#from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    # PERSONAL INFORMATION
    name                    = models.CharField(null=False, blank=False, max_length=50, verbose_name='NOMBRE')
    last_name               = models.CharField(null=False, blank=False, max_length=50, verbose_name='APELLIDOS')
    rut                     = models.CharField(null=False, blank=False, max_length=12, unique=True, verbose_name='RUT (sin puntos, solo guión)')
    birth_day               = models.DateField(null=False, blank=False, verbose_name='FECHA DE NACIMIENTO')
    address                 = models.CharField(null=False, blank=False, max_length=50, verbose_name='DIRECCIÓN')
    city                    = models.CharField(null=False, blank=False, max_length=50, verbose_name='CIUDAD')

    # INSTITUTIONAL INFORMATION
    enrollment_date         = models.DateField(null=False, blank=False, verbose_name='FECHA DE INGRESO')
    GRADE_CHOICES           = [
        ('1B','1ro Básico'),
        ('2B', '2do Básico'),
        ('3B', '3ro Básico'),
        ('4B', '4to Básico'),
        ('5B', '5to Básico'),
        ('6B', '6to Básico'),
        ('7B', '7mo Básico'),
        ('8B', '8vo Básico'),
        ('1M', '1ro Medio'),
        ('2M', '2do Medio'),
        ('3M', '3ro Medio'),
        ('4M', '4to Medio'),
    ]
    grade                   = models.CharField(choices=GRADE_CHOICES, max_length=3, verbose_name='CURSO')
    institutional_email     = models.EmailField(null=False, blank=True, verbose_name='CORREO ELECTRÓNICO INSTITUCIONAL (opcional)')

    class Meta:
        verbose_name        = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return f'{self.last_name}, {self.name} - {self.rut} - {self.birth_day}'
    

class Teacher(models.Model):
    last_name           = models.CharField(null=False, blank=False, max_length=50, verbose_name='Apellidos')
    name                = models.CharField(null=False, blank=False, max_length=50, verbose_name='Nombre')
    rut                 = models.CharField(null=False, blank=False, max_length=12, verbose_name='RUT')
    address             = models.CharField(null=False, blank=False, max_length=50, verbose_name='Dirección')
    city                = models.CharField(null=False, blank=False, max_length=50, verbose_name='Ciudad')
    academic_degree     = models.CharField(null=False, blank=False, max_length=50, verbose_name='Título Académido')
    phone_number        = models.CharField(null=True, blank=True, max_length=12, verbose_name='Número Telefónico (opcional)')

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return f'{self.last_name}, {self.name} - {self.rut} - {self.academic_degree} - {self.phone_number}'