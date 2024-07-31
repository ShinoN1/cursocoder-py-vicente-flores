from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "saoapp/inicio.html")

def cursos(request):
    return render(request, "saoapp/curso.html")

def estudiantes(request):
    return render(request, "saoapp/estudiante.html")

def profesores(request):
    return render(request, "saoapp/profesores.html")

def entregables(request):
    return render(request, "saoapp/entregables.html")


def contact(request):
    if request.method == 'POST':
        return HttpResponse("Formulario de contacto enviado.")
    return render(request, "saoapp/contact.html")