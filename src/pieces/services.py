from pieces.models import Pieces


class GetListMovementsService:

    BOARD = [
        ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
        ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
        ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
        ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
        ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
        ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
        ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
    ]

    ROW = ['8', '7', '6', '5', '4', '3', '2', '1']
    COL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    KNIGHT_ROW_MOVE = [2, 1, -1, -2, -2, -1, 1, 2, 2]
    KNIGHT_COL_MOVE = [1, 2, 2, 1, -1, -2, -2, -1, 1]

    def __init__(self, piece_id, cell):
        self.piece_id = piece_id
        self.cell = cell

    def _is_knight(self):
        try:
            piece = Pieces.objects.get(pk=self.piece_id)
            if piece.name == 'knight':
                return True
        except Pieces.DoesNotExist:
            return False

    def get_list_movements(self):
        if self._is_knight():
            moves = self._calculate()
            return moves
        return 'Piece is not a knight'

    def _calculate(self):
        moves = []
        start_col = self.COL.index(self.cell[0])
        start_row = self.ROW.index(self.cell[1])
        # 8 is quantity possible movements to knight
        for i in range(8):
            new_row = start_row + self.KNIGHT_ROW_MOVE[i]
            new_col = start_col + self.KNIGHT_COL_MOVE[i]
            if self._in_board(new_row, new_col):
                moves.append(self.BOARD[new_row][new_col])
        return moves

    def _in_board(self, row, col):
        # 8 is the length of board is possible be dinamic
        if (row < 0 or col < 0 or row >= 8 or col >= 8):
            return False
        return True
