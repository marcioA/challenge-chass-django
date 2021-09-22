from django.db import models
from uuid import uuid4

# Create your models here.

class Pieces(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    piece_name = models.CharField(max_length=255)
    initial_position = models.CharField(max_length=3)
    current_position = models.CharField(max_length=3)
    previous_position = models.CharField(max_length=3)
    next_positions = models.CharField(max_length=255)
    nice_play = models.BooleanField(default=False)


# id
# piece_name
# piece_color
# initial_position
# current_position
# previous_position
# next_positions
