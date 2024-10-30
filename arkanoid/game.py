import pygame

from . import ANCHO, ALTO


class Arkanoid:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        """
        Bucle principal
        """

        salir = False

        while not salir:
            for evento in pygame.event.get():
                if pygame.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((99, 0, 0))
            pygame.display.flip()
            
        pygame.quit()

if __name__ == '__main__':
    print('Arrancamos el juego desde game.py')
    juego = Arkanoid()
    juego.jugar