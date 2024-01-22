import pygame
from game import play_chess, BOARD_SIZE, CELL_SIZE

LEFT_MARGIN = CELL_SIZE * 2
RIGHT_MARGIN = CELL_SIZE * 4
BUTTON_HEIGHT = CELL_SIZE

BUTTON_WHITE_SHIFT = CELL_SIZE * 2
BUTTON_BLACK_SHIFT = CELL_SIZE * 3.5
BUTTON_TOGETHER_SHIFT = CELL_SIZE * 5


pygame.init()

menu_font = pygame.font.SysFont('Verdana', 15)
menu_text_color = pygame.Color('red')
menu_color = pygame.Color('gray')


def show_menu():
    screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    background = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
    background.fill(pygame.Color(140, 255, 255))

    button_white = pygame.Rect(LEFT_MARGIN, BUTTON_WHITE_SHIFT, RIGHT_MARGIN, BUTTON_HEIGHT)
    text_white = menu_font.render('Play for white', True, menu_text_color)

    button_black = pygame.Rect(LEFT_MARGIN, BUTTON_BLACK_SHIFT, RIGHT_MARGIN, BUTTON_HEIGHT)
    text_black = menu_font.render('Play for black', True, menu_text_color)

    button_together = pygame.Rect(LEFT_MARGIN, BUTTON_TOGETHER_SHIFT, RIGHT_MARGIN, BUTTON_HEIGHT)
    text_together = menu_font.render('Play together', True, menu_text_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_white.collidepoint(event.pos):
                    play_chess(solo_game=False, computer_color=False)
                elif button_black.collidepoint(event.pos):
                    play_chess(solo_game=False, computer_color=True)
                elif button_together.collidepoint(event.pos):
                    play_chess(solo_game=True)

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, menu_color, button_white)
        screen.blit(text_white, text_white.get_rect(center=button_white.center))

        pygame.draw.rect(screen, menu_color, button_black)
        screen.blit(text_black, text_black.get_rect(center=button_black.center))

        pygame.draw.rect(screen, menu_color, button_together)
        screen.blit(text_together, text_together.get_rect(center=button_together.center))
        pygame.display.update()


show_menu()
