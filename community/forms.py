from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name'                        : forms.TextInput(attrs={'class':'control','placeholder':'Ingrese Nombre Alumno'}),
            'last_name'                   : forms.TextInput(attrs={'class':'control','placeholder':'Ingrese Apellido Alumno'}),
            'rut'                         : forms.TextInput(attrs={'class':'control','placeholder':'Ingrese RUT Alumno(sin puntos y con guión)'}),
            'birth_day'                   : forms.DateInput(attrs={'class':'control','placeholder':'Ingrese Fecha Nacimiento Alumno'}),
            'address'                     : forms.TextInput(attrs={'class':'control','placeholder':'Ingrese Dirección Alumno'}),
            'enrollment_day'              : forms.DateInput(attrs={'class':'control','placeholder':'Fecha Ingreso Alumno'}),
            'grade'                       : forms.TextInput(attrs={'class':'control','placeholder':'Curso Que Ingresa Alumno'}),
            'institutional_email'         : forms.EmailInput(attrs={'class':'control','placeholder':'Ingrese Correo Institucional (opcional)'}),
        }