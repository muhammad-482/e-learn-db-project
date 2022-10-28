from ast import mod
from enum import unique
from pyexpat import model
from turtle import mode, title
from unicodedata import category, name
from django.db import models

class Level(models.Model):
    year = models.IntegerField(blank = True, null = True)
    category = models.CharField(max_length=30, blank = True, null = True)


class Subject(models.Model):
    name = models.CharField(max_length=30, blank = True, null = True)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Lesson(models.Model):
    title = models.CharField(max_length=30, blank = True, null = True)
    description = models.CharField(max_length=100000000000000, blank = True, null = True)
    content = models.URLField(max_length=2000000, blank = True, null = True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.title)

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30, blank = True, null = True)
    last_name = models.CharField(max_length=30, blank = True, null = True)
    middle_name = models.CharField(max_length=30, blank = True, null = True)
    phone_number = models.IntegerField(unique = True, blank = True, null = True)
    city = models.CharField(max_length=30, blank = True, null = True)  
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, blank = True, null = True)
    birthdate = models.DateField(blank = True, null = True)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Instructor(models.Model):
    first_name = models.CharField(max_length=30, blank = True, null = True)
    last_name = models.CharField(max_length=30, blank = True, null = True)
    middle_name = models.CharField(max_length=30, blank = True, null = True)
    phone_number = models.IntegerField(unique = True, blank = True, null = True)
    description = models.CharField(max_length=100000, blank = True, null = True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teach(models.Model):
     Instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
     subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Enroll(models.Model):
     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
     subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)



    


