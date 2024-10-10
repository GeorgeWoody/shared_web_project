from django import  forms

from .models import Student, Representative

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        