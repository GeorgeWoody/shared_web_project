### MODELS OF THE SCHOOL COMMUNITY
### STUDENT                 (must be attached to "legal guardian" in some way)
### LEGAL GUARDIAN          (must be attached to "student" in some way)
### TEACHER                 (must be attached to "grades" in some way)
### GRADE                   (must be attached to a group of "students" in some way)
### OTHER PERSONNEL

from django.db import models

class Student(models.Model):
    # PERSONAL INFORMATION
    name                    = models.CharField(null=False, blank=False, max_length=50, verbose_name='NOMBRE')
    last_name               = models.CharField(null=False, blank=False, max_length=50, verbose_name='APELLIDOS')
    rut                     = models.CharField(null=False, blank=False, max_length=12, unique=True, verbose_name='RUT (sin puntos, solo guión)')
    birth_day               = models.DateField(null=False, blank=False, verbose_name='FECHA DE NACIMIENTO')
    address                 = models.CharField(null=False, blank=False, max_length=50, verbose_name='DIRECCIÓN')

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
    institutional_email     = models.EmailField(null=False, blank=True, verbose_name='CORREO ELECTRÓNICO (opcional)')

    class Meta:
        verbose_name        = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return f'{self.last_name}, {self.name} - {self.rut} - {self.birth_day}'
