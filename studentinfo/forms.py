from django import  forms
from django.forms import inlineformset_factory

from .models import Student, Representative


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = 'rut', 'lname', 'name', 'address', 'phone'
        
#        widgets = {
#            'representative': forms.CheckboxSelectMultiple,  # Este widget te permitirá seleccionar múltiples apoderados
#        }
        
class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = 'rep_rut', 'rep_lname', 'rep_name', 'address'
        
RepresentativeFormSet = inlineformset_factory(Student, Student.representative.through, form=RepresentativeForm, extra=1)