from django.urls import path
from saoapp import views

urlpatterns = [
    path('', views.inicio, name='home'),  
    path('cursos/', views.cursos, name='curso'), 
    path('estudiantes/', views.estudiantes, name='estudiante'),  
    path('profesores/', views.profesores, name='profesor'),  
    path('entregables/', views.entregables, name='entregable'),
    path('contact/', views.contact, name='contact'), 
]
