from django.db import models


class Pieces(models.Model):

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    class Meta:
        models.UniqueConstraint(fields=['name', 'color'], name='unique_piece')

    def __str__(self):
        return f'{self.id} - {self.name}'
