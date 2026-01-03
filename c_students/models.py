from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='c_students/', null=True, blank=True)

    def __str__(self):
        return self.name
