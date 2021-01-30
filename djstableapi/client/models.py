from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=40)
    college = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    