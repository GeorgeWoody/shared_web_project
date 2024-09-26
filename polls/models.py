from django.db import models

class Question(models.Model):
    question_text = models.Charfield(max_length=50)
    