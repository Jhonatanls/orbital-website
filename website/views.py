from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
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