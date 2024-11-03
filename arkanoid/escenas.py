import os
import pygame as pg

from . import ALTO, ANCHO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        """
        Este método debe ser implementado por todas y cada una de las escenas 
        en función de lo que estén esperando hasta la condición de salida
        del bucle de la escena
        """
        print('Método vacío bucle principal de escena')

class Portada (Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('resources', 'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

        ruta_letra = os.path.join('resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.tipo_letra = pg.font.Font(ruta_letra, 25)

    def bucle_principal(self):
        super().bucle_principal()

        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

                self.pantalla.fill((99, 0, 0))

                self.pintar_logo()
                self.pintar_mensaje()

                pg.display.flip()

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO - ancho)/2
        pos_y = (ALTO - alto)/2
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_mensaje(self):
        mensaje = 'Pulsa <ESPACIO> para comenzar la partida'
        img_texto = self.tipo_letra.render(mensaje, True, (255, 255, 255))
        pos_x = (ANCHO - img_texto.get_width())/2
        pos_y = 5/6 * ALTO
        self.pantalla.blit(img_texto, (pos_x, pos_y))


class Partida(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((0, 99, 0))
            pg.display.flip()


class Mejores_jugadores(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()

        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
