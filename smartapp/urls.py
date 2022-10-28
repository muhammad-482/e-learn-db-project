from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('', home),
    path('level/<int:id>/',level,name="level"),   
    path('subject/<int:id>/',subject,name="subject" ), 
    path('lesson/<int:id>/',lesson,name="lesson"),          
]
