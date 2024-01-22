import pygame
from board import BOARD_SIZE, CELL_SIZE

pygame.font.init()
pygame.init()


window_surface = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
background = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
background.fill(pygame.Color(140, 255, 255))


button_font = pygame.font.SysFont('Verdana', 15)
button_text_color = pygame.Color("red")
button_color = pygame.Color("gray")
button = pygame.Rect(CELL_SIZE, 200, 300, 50)
button_text1 = button_font.render('Menu!', True, button_text_color)


def end(board):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.collidepoint(event.pos):
                    return
            window_surface.blit(background, (0, 0))
            pygame.draw.rect(window_surface, button_color, button)
            button_center = button_text1.get_rect(center=button.center)
            window_surface.blit(button_text1, button_center)

            f1 = pygame.font.Font(None, 36)
            if board.outcome().winner is True:
                text = f1.render('White win', True, (180, 70, 0))
            else:
                text = f1.render('Black win', True, (180, 70, 0))
            window_surface.blit(text, (140, 50))
            pygame.display.update()

