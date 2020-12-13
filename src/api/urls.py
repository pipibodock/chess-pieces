from django.urls import path

from api import views


urlpatterns = [
    path('',
         views.PiecesView.as_view(), name='pieces'),
    path('<int:pk>/',
         views.PieceView.as_view(), name='piece'),
    path('moves/',
         views.ListMovementsView.as_view(), name='movements'),
]
