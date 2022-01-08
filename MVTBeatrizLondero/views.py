from django.http import HttpResponse
from AppMVT.models import Parientes
from django.template import loader


def muestro_parientes(request):
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