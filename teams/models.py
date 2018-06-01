from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# class Team(models.Model):
#     title = models.CharField(max_length=20)

#     def __str__(self):
#         return self.title

User = settings.AUTH_USER_MODEL

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    randomize_team = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)

class Team(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='teams', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()
    shuffle_answers = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    

class Student(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)