from django.db import models


class Pieces(models.Model):

    piece_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name}'
