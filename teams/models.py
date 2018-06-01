from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models

# class Team(models.Model):
#     title = models.CharField(max_length=20)

#     def __str__(self):
#         return self.title



class Quiz(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    randomize_team = models.BooleanField(default=False)
    number_of_participants = models.IntegerField(default=0)
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
    number_of_responses = models.IntegerField(default=0)

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    
class Student(models.Model):
    team = models.ForeignKey(Team, related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Student_Response(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    response = models.ForeignKey(Answer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

