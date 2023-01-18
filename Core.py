import pygame
from character import Character
from enemys import Enemys

pygame.init()

screen_size = [1024,512]

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("Paralel evrenden gelen Oyun")

surf = pygame.Surface((1024, 512))

clock = pygame.time.Clock()

running = True
mode = "login"

lvl = 1

play_button_rect = pygame.Rect(350, 300, 100, 50)
font = pygame.font.Font(None, 30)

enemys = Enemys(0,screen_size)
character = Character(screen_size,enemys,lvl)
enemys = Enemys(screen_size,character)

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (surf.get_width(), surf.get_height()))

background_rect = background_image.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_size = [event.w, event.h]
            screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
            character = Character(screen_size,enemys,lvl)
            background_image = pygame.transform.scale(background_image, (surf.get_width(), surf.get_height()))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "login" and play_button_rect.collidepoint(event.pos):
                mode = "game"
    if mode == "login":
        screen.fill((255, 255, 255))
        play_button_rect.center = screen.get_rect().center
        pygame.draw.rect(screen, (0, 0, 0), play_button_rect)
        play_text = font.render("<-OYNA->", True, (255, 255, 255))
        play_text_rect = play_text.get_rect()
        play_text_rect.center = play_button_rect.center
        screen.blit(play_text, play_text_rect)
    elif mode == "game":
        surf.blit(background_image, background_rect)

        enemys.update(character.alanrct)
        enemys.draw(surf)
        
        character.update()
        character.draw(surf)
        
        screen.blit(pygame.transform.scale(surf,(screen_size)),(0,0))
    pygame.display.update()
    clock.tick(60)
