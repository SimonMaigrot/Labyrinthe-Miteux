import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self):
        self.image_1 = pygame.image.load("assets/map/map_1.png")
        self.rect = self.image_1.get_rect()
        self.rect.x = 0
        self.rect.y = 0