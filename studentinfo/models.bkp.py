from django.db import models

class Student(models.Model):
    rut = models.CharField(max_length=12, unique=True, null=False, blank=False, verbose_name="RUT")
    lname = models.CharField(max_length=50, null=False, blank=False, verbose_name="Apellidos")
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombres")
    bday = models.DateField(null=False, blank=False, verbose_name="Fecha de Nacimiento")
    address = models.CharField(max_length=250, null=False, blank=False, verbose_name="Domicilio")
    phone = models.CharField(max_length=15, null=False, blank=False, verbose_name="Número de Teléfono")
    email = models.EmailField(null=True, blank=True, verbose_name="Correo Electrónico")
    ins_email = models.EmailField(verbose_name="Correo Institucional", null=True, blank=True) 
    entry_date = models.DateField(null=False, blank=False, verbose_name="Fecha de Ingreso")
    actual_grade = models.ForeignKey("Grade", on_delete=models.SET_NULL, null=True, verbose_name="Curso")
    representative = models.ManyToManyField("Representative", blank=False, verbose_name="Apoderado")

    def __str__(self): 
       return f'{self.rut} - {self.lname}, {self.name} - {self.actual_grade} - {self.ins_email}'

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        
#   "__str__" define cómo se representará el objeto como una "cadena" cuando se haga referencia a él, 
#   por ejemplo, al verlo en el panel de administración de Django o en la consola interactiva.
#   No afecta cómo se almacenan los datos en la base de datos, ésta función define cómo se muestra el "objeto"
#   cuando es convertido a texto. Hace que las entradas de tus modelos sean legibles en el administrador de Django.
# 
#   Ejemplo, tienes un modelo Alumno con campos:
#       name
#       lname 
#       bday
#       
#       cuando accedes a la lista de objetos en el admin de Django, verás algo como:
#           "Alumno object (1)""
#       
#       Pero si defines el metodo __str__ de la siguiente manera:
# 
#       def __str__(self):
#           return f'{self.name} {self.lname} {self.bday}'
#       Entonces, en el admin de Django, verás algo como:
#           Juan Pérez 2005-06-23    

class Representative(models.Model):
    rep_rut = models.CharField(max_length=12, unique=True, null=False, blank=False, verbose_name="RUT")
    rep_lname = models.CharField(max_length=50, null=False, blank=False, verbose_name="Apellidos")
    rep_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombres")
    rep_address = models.CharField(max_length=250, null=False, blank=False, verbose_name="Domicilio")
    rep_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Número Contacto")
    rep_email = models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
    
    def __str__(self):
        return f'{self.rep_rut} - {self.rep_lname}, {self.rep_name}'
    
    class Meta:
        verbose_name = "Apoderados"
        verbose_name_plural = "Apoderados"
class Grade(models.Model):
    grade_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.grade_name
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

#   Campos de un modelo sean opcionales
#       blank=True: Permite que el formulario acepte un valor vacío cuando se está creando o actualizando un objeto.
#       null=True: Permite que la base de datos acepte valores NULL para ese campo. Útil para campos no obligatorios 
#       que pueden quedarse vacíos.  
#   Regla General:
#       Para campos tipo texto (CharField, EmailField, etc.):
#       blank=True: si quieres permitir que el campo esté vacío en los formularios, pero no uses 
#       null=True porque en Django, los campos de texto usan cadenas vacías ("") para representar
#       valores vacíos en lugar de NULL.
#   Para campos que no son de texto (como DateField o ForeignKey), usa tanto null=True como
#       blank=True si quieres permitir que el campo esté vacío.
  
class Subject(models.Model):
    subject_name = models.CharField(max_length=50, verbose_name="Asignaturas")
    description = models.TextField(verbose_name="Descripción")
        
    def __str__(self):
        return self.subject_name  
    
    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

class Teacher(models.Model):
    trut =      models.CharField(max_length=12, null=False, blank=False, unique=True, verbose_name="RUT")
    tlname =    models.CharField(max_length=50, null=False, blank=False, verbose_name="Apellidos")
    tname =     models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombres")
    address =   models.CharField(max_length=250, null=False, blank=False, verbose_name="Domicilio")
    tphone =    models.CharField(max_length=12, null=True, blank=True, verbose_name="Número de Contacto")
    temail =    models.EmailField(null=True, blank=True, verbose_name="Correo")
    tins_email = models.EmailField(null=True, blank=True, verbose_name="Correo Institucional")
    
    def __str__(self):
        return f'RUT: {self.trut} - Nombre: {self.tlname}, {self.tname} - Correo: {self.temail}'

    class Meta:
        verbose_name = "Profesor/a"
        verbose_name_plural = "Profesores/as"
        ordering = ["tlname", "tname"]