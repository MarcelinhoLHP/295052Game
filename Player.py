import pygame

ALTURA = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, jump_sound):
        super().__init__()
        self.image = pygame.image.load("./assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (100, ALTURA - 150)
        self.vel_y = 0
        self.no_chao = False
        self.jump_sound = jump_sound

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.no_chao:
            self.pular()

        self.vel_y += 1
        self.rect.y += self.vel_y

        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
            self.vel_y = 0
            self.no_chao = True

    def pular(self):
        if self.no_chao:
            self.vel_y = -15
            self.no_chao = False
            self.jump_sound.play()
