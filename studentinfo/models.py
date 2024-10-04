from django.db import models

class Student(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    lname = models.CharField(max_length=50, verbose_name="Apellidos")
    name = models.CharField(max_length=50, verbose_name="Nombres")
    bday = models.DateField(verbose_name="Fecha de Nacimiento")
    address = models.CharField(max_length=250, verbose_name="Domicilio")
    phone = models.CharField(max_length=15, verbose_name="Número de Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")
    ins_email = models.EmailField(verbose_name="Correo Institicional", blank=True) 
    entry_date = models.DateField(verbose_name="Fecha de Ingreso")
    actual_grade = models.ForeignKey("Grade", on_delete=models.SET_NULL, null=True, verbose_name="Curso")
    
    def __str__(self): 


       return f'{self.name} {self.lname} {self.bday}'

# El propósito de __str__ es definir cómo se representará el objeto como una cadena cuando se haga referencia a él, por ejemplo, al verlo en el panel de administración de Django o en la consola interactiva.

# Así que, en lugar de afectar cómo se almacenan los datos en la base de datos, esta función define cómo se muestra el objeto cuando es convertido a texto. Esto puede hacer que las entradas de tus modelos sean más legibles y comprensibles en el administrador de Django.
# 
# Por ejemplo, si tienes un modelo Alumno con campos como name, lname (apellido), y bday (fecha de nacimiento), cuando accedas a la lista de objetos en el admin de Django, verás algo como:
 
# "Alumno object (1)""
# Pero si defines el método __str__ de la siguiente manera:
# 
# def __str__(self):
#     return f'{self.name} {self.lname} {self.bday}'
# Entonces, en el admin de Django, verás algo como:
# 
#               Juan Pérez 2005-06-23    
class Grade(models.Model):
    grade_name = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.grade_name
    
    
    
# En Django, para hacer que los campos de un modelo sean opcionales,
#  puedes utilizar los siguientes parámetros en cada campo:
#  blank=True: Permite que el formulario acepte un valor vacío cuando se está creando o actualizando un objeto.
#  null=True: Permite que la base de datos acepte valores NULL para ese campo. Esto es útil para
#  campos no obligatorios que pueden quedarse vacíos.
#  La regla general es:
#  
#  Para campos de tipo texto (CharField, EmailField, etc.), usa blank=True si quieres permitir 
#  que el campo esté vacío en los formularios, pero no uses null=True porque en Django, los campos de 
#  texto usan cadenas vacías ("") para representar valores vacíos en lugar de NULL.
#  
#  Para campos que no son de texto (como DateField o ForeignKey), 
#  usa tanto null=True como blank=True si quieres permitir que el campo esté vacío.

