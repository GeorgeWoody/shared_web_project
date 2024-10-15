from django.urls import path

from .views import index

urlpatterns = [
    path('index/', index, name='index') ### No olvidar incluir la "APP" en settings, si no, la plantilla no cargará ###
]


### RECORDAR: EVENTUALMENTE MOVER LAS FUNCIONALIDADES DE LA APP "INDEX" 
### A "CORE". INVESTIGAR SI ES CONVENIENTE O NO