from django.shortcuts import render, redirect

#from community.models import Student
from community.forms import StudentForm


def community_students_add(request):
    if request.method == 'POST':
        form_student_add = StudentForm(request.POST)
        if form_student_add.is_valid():
            form_student_add.save()
            return redirect("community_student_add_success.html")
        else:
            form_student_add = StudentForm
    return render(request, "community_student_add_error.html")
