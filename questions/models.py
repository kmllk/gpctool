from django.db import models

# Create your models here.
class Question_schema(models.Model):
    question_number = models.AutoField(primary_key=True)
    question_num = models.PositiveSmallIntegerField()
    question_text = models.CharField(max_length=200)
    yes_answer_text = models.CharField(max_length=200, blank=True)
    no_answer_text = models.CharField(max_length=200, blank=True)
    yes_answer = models.PositiveSmallIntegerField()
    no_answer = models.PositiveSmallIntegerField()
