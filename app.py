import pygame
import chess

board = chess.Board()

pygame.init()

CELLS_DEAGONALLY = 8
SQUARE_SIZE = 50
BOARD_SIZE = CELLS_DEAGONALLY * SQUARE_SIZE

screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

piece_images = {}
piece_files = {
    'r': 'black_rook.png',
    'n': 'black_knight.png',
    'b': 'black_bishop.png',
    'q': 'black_queen.png',
    'k': 'black_king.png',
    'p': 'black_pawn.png',
    'R': 'white_rook.png',
    'N': 'white_knight.png',
    'B': 'white_bishop.png',
    'Q': 'white_queen.png',
    'K': 'white_king.png',
    'P': 'white_pawn.png'
}
for symbol, filename in piece_files.items():
    image = pygame.image.load(f'images/{filename}')
    scaled_image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    piece_images[symbol] = pygame.transform.scale(scaled_image, (SQUARE_SIZE, SQUARE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pygame.mouse.get_pos()
                selected_row = click_pos[1] // SQUARE_SIZE
                selected_col = click_pos[0] // SQUARE_SIZE
                selected_square = chess.square(selected_col, CELLS_DEAGONALLY - selected_row - 1)

                if not 'selected_piece' in globals():
                    piece = board.piece_at(selected_square)
                    if piece and piece.color == board.turn:
                        selected_piece = selected_square
                elif 'selected_piece' in globals() and selected_square == selected_piece:
                    del selected_piece
                else:
                    piece = board.piece_at(selected_square)
                    if piece and piece.color == board.turn:
                        selected_piece = selected_square
                    else:
                        uci = chess.square_name(selected_piece) + chess.square_name(selected_square)
                        move = chess.Move.from_uci(uci)
                        if move in board.legal_moves:
                            board.push(move)
                            del selected_piece

    background = pygame.image.load('images/board.png')
    background = pygame.transform.scale(background, (BOARD_SIZE, BOARD_SIZE))
    screen.blit(background, (0, 0))
    move_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
    move_surface.set_alpha(128)
    move_surface.fill(GREEN)
    for row in range(CELLS_DEAGONALLY - 1, -1, -1):
        for col in range(CELLS_DEAGONALLY - 1, -1, -1):
            square = chess.square(col, CELLS_DEAGONALLY - row - 1)
            piece = board.piece_at(square)
            if piece is not None:
                symbol = piece.symbol()
                image = piece_images.get(symbol, None)
                if image:
                    screen.blit(image, (SQUARE_SIZE * col, SQUARE_SIZE * row))

            if 'selected_piece' in globals() and square == selected_piece:
                screen.blit(move_surface, (SQUARE_SIZE * col, SQUARE_SIZE * row))

            if 'selected_piece' in globals() and selected_piece != square:
                moves_from_selected = [move for move in board.legal_moves if move.from_square == selected_piece]
                for move in moves_from_selected:
                    if move.to_square == square:
                        pygame.draw.rect(screen, GREEN, (SQUARE_SIZE * col, SQUARE_SIZE * row, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.update()

pygame.quit()
