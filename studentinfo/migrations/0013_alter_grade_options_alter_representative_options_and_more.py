# Generated by Django 5.1.1 on 2024-10-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0012_rename_subjects_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='representative',
            options={'verbose_name': 'Apoderados', 'verbose_name_plural': 'Apoderados'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Asignatura', 'verbose_name_plural': 'Asignaturas'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['tlname', 'tname'], 'verbose_name': 'Profesor/a', 'verbose_name_plural': 'Profesores/as'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='tins_email',
            field=models.EmailField(default='a@a.a', max_length=254, verbose_name='Correo Institucional'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='temail',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='trut',
            field=models.CharField(max_length=12, unique=True, verbose_name='RUT'),
        ),
    ]
