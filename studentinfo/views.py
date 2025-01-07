from django.shortcuts import render, redirect

from studentinfo.models import Student


#from .forms import StudentForm, RepresentativeFormSet
#from .models import Student

def student_home(request):
    return render(request, 'studentinfo/student_home.html')

def student_search(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(name__icontains=query)
    return render(request, 'studentinfo/student_search.html')

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
#     return render(request, 'studentinfo/add_student.html',
#     {'student_form':student_form},{'representative_form': representative_formset})
#
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'studentinfo/student_list.html', {'students':students})



#def add_teacher(request):
#    if request.method:

#def add_grade(request):
#    if request.method: