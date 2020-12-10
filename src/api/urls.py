from django.urls import path

from api import views


urlpatterns = [
    path('pieces/',
         views.PiecesView.as_view(), name='pieces'),
    path('piece/<int:pk>/',
         views.PieceView.as_view(), name='piece'),
]
