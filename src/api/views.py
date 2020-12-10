from rest_framework import generics

from pieces.models import Pieces
from api.serializers import PiecesSerializer


class PiecesView(generics.ListCreateAPIView):
    queryset = Pieces.objects.all()
    serializer_class = PiecesSerializer


class PieceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pieces.objects.all()
    serializer_class = PiecesSerializer
