from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    return HttpResponse("Contacto")