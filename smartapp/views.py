from http.client import HTTPResponse
from django.shortcuts import render
from .models import *

def hello(request):
    return render(request, 'smartapp/index.html',)

def home(request):
    levels = Level.objects.all()
    return render(request, 'smartapp/home.html',{"levels":levels})

def level(request,id):
    subjects = Subject.objects.filter(level_id = id)
    return render(request, 'smartapp/level.html',{"subjects":subjects})

def subject(request,id):
    lessons = Lesson.objects.filter(subject_id = id)
    return render(request, 'smartapp/subject.html',{"lessons":lessons,"subject_id":id})


def lesson(request,id):
    lesson = Lesson.objects.get(subject_id = id)
    print(lesson)
    return render(request, 'smartapp/lesson.html',{"lesson":lesson})
