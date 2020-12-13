from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PiecesSerializer
from pieces.models import Pieces
from pieces.services import GetListMovementsService


class PiecesView(APIView):

    def get(self, request):
        pieces = Pieces.objects.all()
        name = self.request.GET.get('name')
        color = self.request.GET.get('color')
        if name and color:
            pieces = pieces.filter(
                name__icontains=name,
                color__icontains=color,
            )
        serializer = PiecesSerializer(pieces, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PiecesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PieceView(APIView):

    def get_object(self, pk):
        try:
            return Pieces.objects.get(pk=pk)
        except Pieces.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        piece = self.get_object(pk)
        serializer = PiecesSerializer(piece)
        return Response(serializer.data)

    def put(self, request, pk):
        piece = self.get_object(pk)
        serializer = PiecesSerializer(piece, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        piece = self.get_object(pk)
        piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListMovementsView(APIView):

    def get(self, request):
        piece_id = self.request.GET.get('piece_id')
        cell = self.request.GET.get('cell')
        if cell and piece_id:
            service = GetListMovementsService(piece_id, cell)
            return Response(service.get_list_movements())
        queryset = Pieces.objects.all()
        return Response(list(queryset.values()))
