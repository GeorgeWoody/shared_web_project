from django.shortcuts import render, redirect

from django.db.models import Q
"""Función Q de Django: realiza consultas complejas, permitiendo filtrar por varios campos a la vez"""

from studentinfo.models import Student
from .forms import StudentForm

#from .models import Student

def student_home(request):
    return render(request, 'studentinfo/student_home.html')

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm
    return render(request, 'studentinfo/student_add.html', {'form': form})

def student_search(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query)|
            Q(lname__icontains=query)|
            Q(rut__icontains=query)
        )
        """Se ha importado Q de django.db.models, que permite combinar condiciones en una consulta de manera flexible.
           La consulta busca en los tres campos: name, lname y rut. Se usa | (OR) para que la consulta filtre por 
           cualquier campo que contenga la cadena query."""

    else:                                                                   # Si no hay consulta...
        students = Student.objects.all()                                    # Mostrar todos los estudiantes.

    context = {
        'query':query,
        'students':students
    }

    return render(request, 'studentinfo/student_search.html', context)

# def add_student(request): #Definición de la vista; se encargará de mostrar el formulario y procesar la creación de un nuevo Estudiante. La función recibe el "objeto" "request" como argumento, que contiene toda la información de la solicitud HTTP hecha por el usuario (GET, POST, cookies, etc.).
#     if request.method == 'POST':
#         student_form = StudentForm(request.POST)
#         representative_formset = RepresentativeFormSet(request.POST)
#         if student_form.is_valid() and representative_formset.is_valid():
#             student = student_form.save()
#             representatives = representative_formset.save(commit=False)
#             for representative in representatives:
#                 representative.save()
#                 student.representative.add(representative)
#             return redirect('success')
#     else:
#         student_form = StudentForm()
#         representative_formset = RepresentativeFormSet()
#
#     return render(request, 'studentinfo/student_add.html',
#     {'student_form':student_form},{'representative_form': representative_formset})
#
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'studentinfo/student_list.html', {'students':students})



#def add_teacher(request):
#    if request.method:

#def add_grade(request):
#    if request.method: