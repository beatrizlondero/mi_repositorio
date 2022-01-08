from django.http import HttpResponse
from AppMVT.models import Parientes
from django.template import Template, Context, loader

def muestroParientes(request):
    
    template = loader.get_template('parientes.html')

    documento = template.render(Parientes)

    return HttpResponse(documento)
