from .models import Perris
from rest_framework import serializers

class PerrisSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Perris
        fields = ( 'id', 'nombre', 'raza', 'descripcion', 'state', 'imageUrl' )

