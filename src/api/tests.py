import json

from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APITestCase

from pieces.models import Pieces


class CreatePiecesTestCase(APITestCase):

    def setUp(self):
        self.data = {
            'name': 'knight',
            'color': 'black',
        }

    def test_create_chess_piece(self):
        response = self.client.post(
            reverse('pieces'),
            data=json.dumps(self.data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Pieces.objects.exists())


class ListPiecesTestCase(APITestCase):

    def test_list_pieces_return_200(self):
        response = self.client.get(reverse('pieces'))
        self.assertEqual(response.status_code, 200)

    def test_list_all_chess_pieces(self):
        baker.make(Pieces, _quantity=5)
        response = self.client.get(reverse('pieces'))
        self.assertEqual(len(response.data), 5)

    def test_list_piece_for_name(self):
        baker.make(Pieces, name='bishop', color='white')
        baker.make(Pieces, name='knight', color='white')
        url = reverse('pieces') + '?name=bishop&color=white'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class PiecesDetailTestCase(APITestCase):

    def setUp(self):
        self.piece = baker.make(
            Pieces,
            name='bishop',
            color='white',
        )

    def test_get_piece_return_200(self):
        response = self.client.get(
            reverse('piece', args=[self.piece.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_get_piece_detail(self):
        response = self.client.get(reverse('piece', args=[self.piece.pk]))
        expected_response = {
            'id': 1,
            'name': 'bishop',
            'color': 'white',
        }
        self.assertEqual(set(response.data), set(expected_response))

    def test_update_piece(self):
        new_data = {
            'name': 'bishop',
            'color': 'black',
        }
        response = self.client.put(
            reverse('piece', args=[self.piece.pk]),
            data=json.dumps(new_data),
            content_type='application/json',
        )
        self.piece.refresh_from_db()
        self.assertEqual(response.data['color'], new_data['color'])
        self.assertEqual(self.piece.color, new_data['color'])

    def test_delete_piece(self):
        response = self.client.delete(reverse('piece', args=[self.piece.pk]))
        self.assertIsNone(response.data)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Pieces.objects.all().exists())
