from django.db import models
from quiz.models import Quiz

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        pass

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

