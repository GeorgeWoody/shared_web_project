from django import  forms

from .models import Student, Representative

class StudentForm(forms.ModelForm):
    representative_name =
    
    
    class Meta:
        model = Student
        fields = '__all__'
        