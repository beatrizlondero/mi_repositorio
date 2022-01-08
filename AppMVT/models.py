from django.db.models import Model
from django.db.models.fields import CharField, IntegerField,DateField

class Parientes (Model):
    nombre = CharField (max_length=40)
    parentesco= CharField(max_length=20)
    cumpe = DateField()
    cantidadHijos= IntegerField()
    


