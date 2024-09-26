from django.db import models

class Question(models.Model):
    question_text = models.Charfield(max_length=50)
    pub_date = models.DateTimeField("Fecha de Publicación")
    
class Choice(models.Model):
    question = models.ForeignKey(max_length=200)
    choice_text = models.DateTimeField(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    