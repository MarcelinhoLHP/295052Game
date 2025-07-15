import pygame
import sys
import random
from Player import Player
from Platform import Platform

LARGURA = 800
ALTURA = 600
BRANCO = (255, 255, 255)
FPS = 60

class Game:
    def __init__(self, screen):
        self.bg_image = pygame.image.load("./assets/fundo.jpg").convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 600))
        self.bg_x = 0

        #incorporando o som
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.jump_sound = pygame.mixer.Sound("./assets/jump.mp3")
        pygame.mixer.music.load("./assets/Score.mp3")
        pygame.mixer.music.play(-1)

        self.pontuacao = 0
        self.velocidade = 3
        self.tempo = 0

        self.jogador = Player(self.jump_sound)
        self.plataformas = pygame.sprite.Group()
        self.todas_sprites = pygame.sprite.Group()
        self.todas_sprites.add(self.jogador)

        for i in range(5):
            x = i * 200 + random.randint(0, 100)
            y = ALTURA - random.randint(100, 300)
            plataforma = Platform(x, y, self.velocidade)
            self.plataformas.add(plataforma)
            self.todas_sprites.add(plataforma)

        self.font = pygame.font.SysFont("arial", 30)

        # Atualiza posição do fundo
        self.bg_x -= self.velocidade // 2  # velocidade ajustável


    def run(self):
        while True:
            self.clock.tick(FPS)
            self.tempo += 1
            # Atualiza posição do fundo
            self.bg_x -= self.velocidade // 2  # ajustável

            # Reinicia loop quando uma imagem sair da tela
            if self.bg_x <= -800:
                self.bg_x = 0

            # Desenha o fundo duas vezes, lado a lado
            self.screen.blit(self.bg_image, (self.bg_x, 0))
            self.screen.blit(self.bg_image, (self.bg_x + 800, 0))

            # Desenha os sprites
            self.todas_sprites.draw(self.screen)

            if self.tempo % 300 == 0:
                self.velocidade += 1
                for p in self.plataformas:
                    p.speed = self.velocidade

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.jogador.update()
            self.plataformas.update()

            colisoes = pygame.sprite.spritecollide(self.jogador, self.plataformas, False)
            if colisoes and self.jogador.vel_y > 0:
                self.jogador.rect.bottom = colisoes[0].rect.top
                self.jogador.vel_y = 0
                self.jogador.no_chao = True

            self.pontuacao += 0.1

            self.screen.fill((135, 206, 250))
            self.todas_sprites.draw(self.screen)

            pontos_texto = self.font.render(f"Pontos: {int(self.pontuacao)}", True, BRANCO)
            self.screen.blit(pontos_texto, (10, 10))

            pygame.display.flip()