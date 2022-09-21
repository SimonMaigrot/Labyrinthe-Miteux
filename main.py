import pygame
from player import Player
from map import Map
pygame.init()

# Important
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 144

#Variables
player = Player()
map = Map()
pygame.time.set_timer(pygame.USEREVENT, 300)
counter = 1

'''Boucle jeu'''
running = True
while running:

    ''' Evenements'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.USEREVENT:
            counter += 1

    if counter > 2:
        counter = 0

    '''Déplacements'''
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        # Déplacement
        player.move_up()
        # Animation
        player.image_content = player.tab_up[counter]

    if pressed[pygame.K_DOWN]:
        player.move_down()
        player.image_content = player.tab_down[counter]

    if pressed[pygame.K_LEFT]:
        player.move_left()
        player.image_content = player.tab_left[counter]

    if pressed[pygame.K_RIGHT]:
        player.move_right()
        player.image_content = player.tab_right[counter]


    '''Affichage'''
    screen.blit(screen, (0, 0))
    screen.fill([255, 255, 255])
    screen.blit(map.image_1, map.rect)
    screen.blit(player.image_content, player.rect)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()