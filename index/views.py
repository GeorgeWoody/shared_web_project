from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index/index.html") ### No olvidar incluir la "APP" en settings, si no, la plantilla no cargará ###
#    return render(request, 'index/index.html')


