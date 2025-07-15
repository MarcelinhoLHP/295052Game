import pygame

from Game import Game
from Menu import Menu


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jogo de Pular Pedras")

    menu = Menu(screen)
    opcao = menu.mostrar()

    if opcao == "jogo":
        jogo = Game(screen)
        jogo.run()

if __name__ == "__main__":
    main()