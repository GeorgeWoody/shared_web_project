from django.shortcuts import render, redirect

from .forms import StudentForm

def student_add_view(request):
    if request.method == 'POST':
        student_add_form = StudentForm(request.POST)
        if student_add_form.is_valid():
            student_add_form.save()
            return redirect('student_add')
    else:
        student_add_form = StudentForm()
        return render(request, 'student_info_home.html', {'student_add_form':student_add_form})