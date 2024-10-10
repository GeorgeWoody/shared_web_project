from django.shortcuts import render, redirect

from .forms import StudentForm

def add_student(request): #Definición de la vista; se encargará de mostrar el formulario y procesar la creación de un nuevo Estudiante. La función recibe el "objeto" "request" como argumento, que contiene toda la información de la solicitud HTTP hecha por el usuario (GET, POST, cookies, etc.).
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()    
    return render(request, 'studentinfo/add_student.html', {'form':form})




#def add_teacher(request):
#    if request.method:

#def add_grade(request):
#    if request.method: