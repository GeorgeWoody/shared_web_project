from django import  forms

from .models import Student, Representative

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        widgets = {
            'representative': forms.CheckboxSelectMultiple,  # Este widget te permitirá seleccionar múltiples apoderados
        }