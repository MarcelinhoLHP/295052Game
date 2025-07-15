import pygame
import random

LARGURA = 800
ALTURA = 600

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("./assets/platform.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = LARGURA + random.randint(0, 100)
            self.rect.y = ALTURA - random.randint(100, 300)
