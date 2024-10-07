from django.contrib import admin

from .models import Student, Grade, Representative


class RepresentativeInline(admin.TabularInline):
    model = Student.representative.through
    extra = 1
    
class StudentAdmin(admin.ModelAdmin):
    inline = [RepresentativeInline]
    
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Representative)
admin.site.register(Grade)