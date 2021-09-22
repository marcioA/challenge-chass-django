from rest_framework import serializers
from pieces import models

class PiecesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Pieces
        fields = '__all__'