from django.db import models
from django.db import models
class Blog(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.CharField(max_length=5)

    def _str_(self):
        return self.name

# Create your models here.
