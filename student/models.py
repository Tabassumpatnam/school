from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    mobile = models.CharField(max_length=10)

# Create your models here.
