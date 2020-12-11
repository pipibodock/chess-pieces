from rest_framework import generics

from pieces.models import Pieces
from api.serializers import PiecesSerializer


class PiecesView(generics.ListCreateAPIView):
    serializer_class = PiecesSerializer

    def get_queryset(self):
        queryset = Pieces.objects.all()
        name = self.request.query_params.get('name')
        color = self.request.query_params.get('color')
        if name and color:
            queryset = queryset.filter(
                name__icontains=name,
                color__icontains=color,
            )
        return queryset


class PieceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pieces.objects.all()
    serializer_class = PiecesSerializer
