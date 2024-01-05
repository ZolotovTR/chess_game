import pygame
import chess


CELLS_ON_BORD_LINE = 8
SQUARE_SIZE = 50
BOARD_SIZE = CELLS_ON_BORD_LINE * SQUARE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
board = chess.Board()
board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))


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
    'P': 'white_pawn.png',
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

    background = pygame.image.load('images/board.png')
    background = pygame.transform.scale(background, (BOARD_SIZE, BOARD_SIZE))
    screen.blit(background, (0, 0))
    for row in range(CELLS_ON_BORD_LINE):
        for col in range(CELLS_ON_BORD_LINE):
            square = chess.square(col, CELLS_ON_BORD_LINE - row - 1)
            piece = board.piece_at(square)
            if piece is not None:
                symbol = piece.symbol()
                image = piece_images.get(symbol, None)
                if image:
                    screen.blit(image, (col * SQUARE_SIZE, (CELLS_ON_BORD_LINE - row - 1) * SQUARE_SIZE))

    pygame.display.update()

pygame.quit()
