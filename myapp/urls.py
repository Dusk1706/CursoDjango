from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('hello/<str:user>',views.hello),   
    path('projects/',views.projects),
    path('tasks/',views.tasks),
    path('create_task/',views.create_task),
]