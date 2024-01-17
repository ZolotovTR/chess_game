import chess

MAX_DEPTH = 3

piece_values = {
    chess.PAWN: 10,
    chess.ROOK: 50,
    chess.KNIGHT: 32,
    chess.BISHOP: 33,
    chess.QUEEN: 90,
    chess.KING: 40
}


def calculate_advantage(board):
    advantage = len(list(board.legal_moves))
    if not advantage:
        return float('-inf')
    for square, piece in board.piece_map().items():
        piece_value = piece_values[piece.piece_type]
        if piece.color == board.turn:
            advantage += piece_value
        else:
            advantage -= piece_value

    return advantage


class Engine:
    def __init__(self, board):
        self.board = board
        self.advantage = 0

    def __call__(self):
        print('-' * 211)
        advantage, move = self.find_best_move(MAX_DEPTH)
        self.board.push(move)

    def find_best_move(self, depth):
        legal_moves = list(self.board.legal_moves)
        if depth == 0 or not legal_moves:
            return calculate_advantage(self.board), None
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
                    print(move, calculate_advantage(self.board), advantage)

                self.board.pop()

            return max_advantage, best_move

