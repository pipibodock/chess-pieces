from model_bakery import baker

from django.test import TestCase
from django.db import IntegrityError

from pieces.models import Pieces


class PiecesTestCase(TestCase):

    def test_is_instance(self):
        pieces = baker.make(Pieces, name='knight')
        self.assertIsInstance(pieces, Pieces)

    def test_create_chess_piece(self):
        baker.make(Pieces, name='knight')
        self.assertTrue(Pieces.objects.filter(name='knight').exists())

    def test_create_repeated_piece_raise_integrity_error(self):
        baker.make(Pieces, name='knight', color='white')
        with self.assertRaises(IntegrityError):
            Pieces.objects.create(name='knight', color='white')
