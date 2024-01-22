import pygame
from app import play_game

pygame.init()

# end = EndGame()

window_surface = pygame.display.set_mode((300, 300))
background = pygame.Surface((300, 300))
background.fill(pygame.Color(140, 255, 255))


button_font = pygame.font.SysFont('Verdana', 15)
button_text_color = pygame.Color("red")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(100, 115, 100, 50)
button_text = button_font.render('Duo!', True, button_text_color)

button_rect1 = pygame.Rect(100, 190, 100, 50)
button_text1 = button_font.render('Solo!', True, button_text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                pygame.quit()
                play_game()
                exit()



        window_surface.blit(background, (0, 0))
        pygame.draw.rect(window_surface, button_color, button_rect)
        button_rect_center = button_text.get_rect(center=button_rect.center)
        window_surface.blit(button_text, button_rect_center)

        pygame.draw.rect(window_surface, button_color, button_rect1)
        button_rect_center1 = button_text1.get_rect(center=button_rect1.center)
        window_surface.blit(button_text1, button_rect_center1)
        pygame.display.update()
