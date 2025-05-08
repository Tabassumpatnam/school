from django.db import models
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.CharField(max_length=5)

    def __str__ (self):
        return self.name

# Create your models here.
