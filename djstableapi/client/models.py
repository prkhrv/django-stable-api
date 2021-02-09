from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=40)
    college = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.name
        
class SoccerInfo(models.Model):
    data = models.JSONField()
    