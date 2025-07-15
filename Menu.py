import pygame
import sys

BRANCO = (255, 255, 255)
AZUL = (50, 150, 255)
LARGURA = 800

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 40)

    def mostrar(self):
        while True:
            self.screen.fill(AZUL)
            titulo = self.font.render("Pular Pedras!", True, BRANCO)
            jogar = self.font.render("1. Jogar", True, BRANCO)
            sair = self.font.render("2. Sair", True, BRANCO)

            self.screen.blit(titulo, (LARGURA // 2 - 120, 100))
            self.screen.blit(jogar, (LARGURA // 2 - 80, 200))
            self.screen.blit(sair, (LARGURA // 2 - 80, 300))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        return "jogo"
                    if evento.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()