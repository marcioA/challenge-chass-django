from rest_framework import viewsets
from pieces.api import serializers
from pieces import models

class PiecesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PiecesSerializers
    queryset = models.Pieces.objects.all()