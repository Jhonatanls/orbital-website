from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm 

def inicio(request):
    return render(request, 'inicio.html', {
    })

def nosotros(request):
    return render(request, 'nosotros.html', {
    })

def cotizar(request):
    return render(request, 'cotizar.html', {
    })

def contact(request):
    form = ContactForm()
    
    return render(request, 'contacto.html', {'form': form})