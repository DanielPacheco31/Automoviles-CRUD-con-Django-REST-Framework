from rest_framework import viewsets
from pachecoApp.models import Automovil
from .serializers import AutomovilSerializer

class AutomovilViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operaciones CRUD en el modelo Automovil.
    """
    queryset = Automovil.objects.all()
    serializer_class = AutomovilSerializer