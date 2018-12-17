from django.db import models

PRIORITIES = [("LOW","LOW"), ("MED","MEDIUM"), ("HIGH","HIGH"), ("URG","URGENT")]

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100)
    email = models.EmailField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    dueDate = models.DateField()
    priority = models.CharField(choices = PRIORITIES, default = "LOW", max_length = 5)
