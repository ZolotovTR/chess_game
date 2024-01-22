import chess

MAX_DEPTH = 3

MOVE_WEIGHT = 2
STALEMATE_WEIGHT = 0
CHECKMATE_WEIGHT = -10 ** 6

piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 400
}


class Engine:
    def __init__(self, board):
        self.board = board
        self.advantage = 0

    def __call__(self):
        print('-' * 211)
        advantage, move = self.find_best_move(MAX_DEPTH)
        if self.board.piece_at(move.to_square):
            self.advantage += piece_values[self.board.piece_at(move.to_square).piece_type]
        self.board.push(move)

        print(f'Engine advantage: {self.advantage}')

    def push(self, move):
        if self.board.piece_at(move.to_square):
            self.advantage -= piece_values[self.board.piece_at(move.to_square).piece_type]
        self.board.push(move)

        print(f'Engine advantage: {self.advantage}')

    def calculate_advantage(self):
        advantage = len(list(self.board.legal_moves)) * MOVE_WEIGHT
        for square, piece in self.board.piece_map().items():
            piece_value = piece_values[piece.piece_type]
            if piece.color == self.board.turn:
                advantage += piece_value
            else:
                advantage -= piece_value

        return advantage

    def find_best_move(self, depth):
        legal_moves = list(self.board.legal_moves)
        if depth == 0:
            return self.calculate_advantage(), None
        else:
            best_move = None
            max_advantage = float('-inf')

            for move in legal_moves:
                self.board.push(move)

                advantage = -self.find_best_move(depth - 1)[0]

                if advantage > max_advantage:
                    max_advantage = advantage
                    best_move = move

                if depth == MAX_DEPTH:
                    print(move, self.calculate_advantage(), advantage)

                self.board.pop()

            return max_advantage, best_move
