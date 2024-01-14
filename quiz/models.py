from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="quiz duration")

    def __str__(self) -> str:
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        pass


