from django.shortcuts import render
from django.http import HttpResponse

from .forms import 

def inicio(request):
    return render(request, 'inicio.html', {
    })

def nosotros(request):
    return render(request, 'nosotros.html', {
    })

def contacto(request):
    return render(request, 'contacto.html', {
    })

def cotizar(request):
    return render(request, 'cotizar.html', {
    })
