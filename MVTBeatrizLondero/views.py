from django.http import HttpResponse
from AppMVT.models import Parientes
from django.template import Template, Context, loader
from datetime import date, datetime

def muestroParientes(request):
    
    template = loader.get_template('parientes.html')

    documento = template.render(Parientes)

    return HttpResponse(documento)

def ejemplo_template(request):
    # for nombre in Parientes.nombre :
    parientes = Parientes(nombre='Alfonos Andrea', parentesco="primo",cumpe='1995-06-06' ,cantidadHijos=2)
    parientes.save()
        
    diccionario = {
        'nombre': parientes.nombre,
        'parentesco': parientes.parentesco,
        'cumple': parientes.cumpe,
        'cantidadHijos': parientes.cantidadHijos,
    }

    template = loader.get_template('parientes.html')

    documento = template.render(diccionario)

    return HttpResponse(documento)