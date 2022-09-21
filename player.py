import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image_up_1 = pygame.image.load("assets/player/up_1.png")
        self.image_up_1 = pygame.transform.scale(self.image_up_1, (64, 64))
        self.image_up_2 = pygame.image.load("assets/player/up_2.png")
        self.image_up_2 = pygame.transform.scale(self.image_up_2, (64, 64))
        self.image_up_3 = pygame.image.load("assets/player/up_3.png")
        self.image_up_3 = pygame.transform.scale(self.image_up_3, (64, 64))
        self.image_up = self.image_up_1
        self.tab_up = [self.image_up_1, self.image_up_2, self.image_up_3]

        self.image_down_1 = pygame.image.load("assets/player/down_1.png")
        self.image_down_1 = pygame.transform.scale(self.image_down_1, (64, 64))
        self.image_down_2 = pygame.image.load("assets/player/down_2.png")
        self.image_down_2 = pygame.transform.scale(self.image_down_2, (64, 64))
        self.image_down_3 = pygame.image.load("assets/player/down_3.png")
        self.image_down_3 = pygame.transform.scale(self.image_down_3, (64, 64))
        self.tab_down = [self.image_down_1, self.image_down_2, self.image_down_3]

        self.image_left_1 = pygame.image.load("assets/player/left_1.png")
        self.image_left_1 = pygame.transform.scale(self.image_left_1, (64, 64))
        self.image_left_2 = pygame.image.load("assets/player/left_2.png")
        self.image_left_2 = pygame.transform.scale(self.image_left_2, (64, 64))
        self.image_left_3 = pygame.image.load("assets/player/left_3.png")
        self.image_left_3 = pygame.transform.scale(self.image_left_3, (64, 64))
        self.tab_left = [self.image_left_1, self.image_left_2, self.image_left_3]

        self.image_right_1 = pygame.image.load("assets/player/right_1.png")
        self.image_right_1 = pygame.transform.scale(self.image_right_1, (64, 64))
        self.image_right_2 = pygame.image.load("assets/player/right_2.png")
        self.image_right_2 = pygame.transform.scale(self.image_right_2, (64, 64))
        self.image_right_3 = pygame.image.load("assets/player/right_3.png")
        self.image_right_3 = pygame.transform.scale(self.image_right_3, (64, 64))
        self.tab_right = [self.image_right_1, self.image_right_2, self.image_right_3]

        self.image_content = self.tab_down[0]
        self.rect = self.image_content.get_rect()
        self.rect.x = 100
        self.rect.y = 50
        self.speed = 1.8

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed