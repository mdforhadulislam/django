from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    roll = models.IntegerField()
    class_name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.name
