from django.db import models
from django.contrib.auth.models import User
import random

WRONG_CHOICES=['public', 'private', 'protected', 'friend'
'this', 'parent', 'base', 'ancestor'
'public', 'private', 'protected', 'static'
'static', 'abstract', 'synchronized', 'volatile'
'abstract', 'default', 'static', 'final'
'class', 'object', 'method', 'function'
'early', 'static', 'compile-time', 'predefined'
'static', 'final', 'immutable', 'constant'
'output', 'return', 'print', 'message'
'Inheritance', 'Encapsulation', 'Composition', 'Polymorphism'
'Overriding', 'Abstracting', 'Refining', 'Redefining'
'Inheritance', 'Aggregation', 'Delegation', 'Instantiation'
'BaseClass', 'Parent', 'Super', 'Root'
'Global', 'Instance', 'Member', 'Public']

class Question(models.Model):
    text=models.CharField(max_length=500)
    correct_answer=models.CharField(max_length=100)
    points=models.IntegerField(default=1)

    def jumbled_choices(self):
        wrongchoices= random.sample(WRONG_CHOICES,3)
        choices=wrongchoices+[self.correct_answer]
        random.shuffle(choices)
        return choices
    def __str__(self):
        return self.text

class Dashboard(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    plays=models.PositiveIntegerField(default=0)
    points=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} -> Points: {self.points}"