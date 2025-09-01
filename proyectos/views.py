from django.shortcuts import render
from django.http import HttpResponse

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista lista de proyectos
def lista_proyectos(request):
    proyectos = [
        {"nombre": "Sistema de Inventario", "descripcion": "App para gestionar stock"},
        {"nombre": "Blog Personal", "descripcion": "Mi espacio de escritura"},
        {"nombre": "Mi Portafolio", "descripcion": "Sitio web con mis proyectos"},
    ]
    return render(request, 'lista_proyectos.html', {"proyectos": proyectos})
