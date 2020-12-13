from model_bakery import baker

from django.test import TestCase
from django.db import IntegrityError

from pieces.models import Pieces
from pieces.services import GetListMovementsService


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


class GetListMovimentsServiceTestCase(TestCase):

    def setUp(self):
        self.piece = baker.make(Pieces, name='knight', color='black')

    def test_is_instance(self):
        service = GetListMovementsService(self.piece.id, 'b8')
        self.assertIsInstance(service, GetListMovementsService)

    def test_get_object_knight(self):
        service = GetListMovementsService(self.piece.id, 'b8')
        self.assertTrue(service._is_knight())

    def test_return_false_objects_does_not_exists(self):
        bishop = baker.make(Pieces, name='bishop', color='black')
        service = GetListMovementsService(bishop.id, 'b8')
        self.assertFalse(service._is_knight())

    def test_list_moviments_return_message_if_not_knight(self):
        bishop = baker.make(Pieces, name='bishop', color='black')
        service = GetListMovementsService(bishop.id, 'b8')
        mensagem_esperada = 'Piece is not a knight'
        self.assertEqual(service.get_list_movements(), mensagem_esperada)

    def test_get_list_movements_to_knight_first_turn_b8(self):
        service = GetListMovementsService(self.piece.id, 'b8')
        response = service.get_list_movements()
        self.assertListEqual(response['first_turn'], ['c6', 'd7', 'a6'])

    def test_get_list_movements_to_knight_first_turn_cell_d5(self):
        service = GetListMovementsService(self.piece.id, 'd5')
        response = service.get_list_movements()
        self.assertListEqual(
            response['first_turn'],
            ['e3', 'f4', 'f6', 'e7', 'c7', 'b6', 'b4', 'c3']
        )

    def test_get_list_movements_to_knight_first_turn_cell_h1(self):
        service = GetListMovementsService(self.piece.id, 'h1')
        response = service.get_list_movements()
        self.assertListEqual(response['first_turn'], ['g3', 'f2'])

    def test_get_list_movements_to_knight_seccond_turn_start_b8(self):
        service = GetListMovementsService(self.piece.id, 'b8')
        response = service.get_list_movements()
        self.assertDictEqual(
            response['seccond_turn'],
            {
                'c6': ['d4', 'e5', 'e7', 'd8', 'b8', 'a7', 'a5', 'b4'],
                'd7': ['e5', 'f6', 'f8', 'b8', 'b6', 'c5'],
                'a6': ['b4', 'c5', 'c7', 'b8']
            }
        )

    def test_get_list_movements_to_knight_seccond_turn_start_h1(self):
        service = GetListMovementsService(self.piece.id, 'h1')
        response = service.get_list_movements()
        self.assertDictEqual(
            response['seccond_turn'],
            {
                'g3': ['h1', 'h5', 'f5', 'e4', 'e2', 'f1'],
                'f2': ['h1', 'h3', 'g4', 'e4', 'd3', 'd1'],
            }
        )

    def test_get_all_list_movements_start_b8(self):
        service = GetListMovementsService(self.piece.id, 'b8')
        response = service.get_list_movements()
        self.assertDictEqual(
            response,
            {
                'first_turn': ['c6', 'd7', 'a6'],
                'seccond_turn': {
                    'c6': ['d4', 'e5', 'e7', 'd8', 'b8', 'a7', 'a5', 'b4'],
                    'd7': ['e5', 'f6', 'f8', 'b8', 'b6', 'c5'],
                    'a6': ['b4', 'c5', 'c7', 'b8']
                }
            }
        )

    def test_get_all_list_movements_start_h1(self):
        service = GetListMovementsService(self.piece.id, 'h1')
        response = service.get_list_movements()
        self.assertDictEqual(
            response,
            {
                'first_turn': ['g3', 'f2'],
                'seccond_turn': {
                    'g3': ['h1', 'h5', 'f5', 'e4', 'e2', 'f1'],
                    'f2': ['h1', 'h3', 'g4', 'e4', 'd3', 'd1'],
                }
            }
        )
