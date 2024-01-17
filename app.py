import pygame
import chess

from board import board, piece_images
from engine import Engine

CELLS_COUNT = 8
CELL_SIZE = 50
GREEN = (0, 128, 0)
BOARD_SIZE = CELLS_COUNT * CELL_SIZE

pygame.init()

screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

computer_color = False
running = True
engine = Engine(board)

while running:
    if computer_color == board.turn:
        engine()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pygame.mouse.get_pos()
                selected_row = click_pos[1] // CELL_SIZE
                selected_col = click_pos[0] // CELL_SIZE
                selected_square = chess.square(selected_col, CELLS_COUNT - selected_row - 1)

                if 'selected_piece' not in globals():
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
    move_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
    move_surface.set_alpha(128)
    move_surface.fill(GREEN)
    for row in range(CELLS_COUNT - 1, -1, -1):
        for col in range(CELLS_COUNT - 1, -1, -1):
            square = chess.square(col, CELLS_COUNT - row - 1)
            piece = board.piece_at(square)
            if piece is not None:
                symbol = piece.symbol()
                image = piece_images.get(symbol, None)
                if image:
                    screen.blit(image, (CELL_SIZE * col, CELL_SIZE * row))

            if 'selected_piece' in globals() and square == selected_piece:
                screen.blit(move_surface, (CELL_SIZE * col, CELL_SIZE * row))

            if 'selected_piece' in globals() and selected_piece != square:
                moves_from_selected = [move for move in board.legal_moves if move.from_square == selected_piece]
                for move in moves_from_selected:
                    if move.to_square == square:
                        surf = pygame.Surface((CELL_SIZE, CELL_SIZE))
                        surf.fill(GREEN)
                        surf.set_alpha(75)
                        screen.blit(surf, (CELL_SIZE * col, CELL_SIZE * row))


    pygame.display.update()

pygame.quit()
