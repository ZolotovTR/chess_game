import chess
import pygame
import os

board = chess.Board()

CELLS_COUNT = 8
CELL_SIZE = 50


GREEN = (0, 128, 0)

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
    image_path = os.path.join('images', filename)
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
    piece_images[symbol] = pygame.transform.scale(scaled_image, (CELL_SIZE, CELL_SIZE))
