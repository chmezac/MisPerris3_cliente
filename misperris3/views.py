from .models import Perris
from rest_framework import viewsets
from misperris3.serializers import PerrisSerializer

# Create your views here.
class PerrisViewSet( viewsets.ModelViewSet ):
    queryset = Perris.objects.all().order_by( 'nombre' )
    serializer_class = PerrisSerializer