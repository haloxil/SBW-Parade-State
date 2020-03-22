from django.db import models
from datetime import datetime
from .choices import *
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    rank = models.CharField(max_length=30, choices=rank_choice, default="PTE")
    date = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=30, choices=status_choice, default="Present")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.rank
