from django.shortcuts import render, redirect
from django.db.models import Q
"""Función Q de Django: realiza consultas complejas, permitiendo filtrar por varios campos a la vez"""

from django.contrib import messages

from .forms import StudentForm
from .models import Student, Teacher

def community_home_view(request):
    return render(request, 'community_home.html')

def community_teacher_list_view(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'teacher_list.html',{'teacher_list':teacher_list})

### Student Section ###

        ### Search ###
def student_search_view(request):
    query = request.GET.get('q', '').strip()
    if query:
        students_instance = Student.objects.filter(
            Q(name__icontains=query)|
            Q(last_name__icontains=query)|
            Q(rut__icontains=query)
        )
    return render(request, 'partials/student_search_result.html',{'students_instance':students_instance})

        ### Add ###
def student_add_view(request):
    if request.method == 'POST':
        student_add_form = StudentForm(request.POST)
        if student_add_form.is_valid():
            student_add_form.save()
            messages.success(request, 'Estudiante Agregado Correctamente') ### Importado de "from django.contrib import messages" ###
            return redirect('student_add')
    else:
        student_add_form = StudentForm()
    return render(request, 'community_home.html', {'student_add_form':student_add_form})

    