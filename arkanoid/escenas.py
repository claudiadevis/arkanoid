import os
import pygame as pg

from . import ALTO, ANCHO, FPS
from .entidades import Ladrillo, Pelota, Raqueta


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

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
                if pg.QUIT == evento.type or (
                    evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                    return True

                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    salir = True

                self.pantalla.fill((99, 0, 0))

                self.pintar_logo()
                self.pintar_mensaje()

                pg.display.flip()
        return False

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
        ruta_fondo = os.path.join('resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta_fondo)
        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.pelota = Pelota(self.jugador)

    def bucle_principal(self):
        super().bucle_principal()

        salir = False
        self.crear_muro()
        juego_iniciado = False

        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if pg.QUIT == evento.type or (
                    evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    juego_iniciado = True
                
            self.pintar_fondo()
            self.muro.draw(self.pantalla)


            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            self.pelota.update(juego_iniciado)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            golpeados = pg.sprite.spritecollide(self.pelota, self.muro, True)
            print('Golpeados:', golpeados)
            
            if len(golpeados) > 0:
                self.pelota.vel_y = -self.pelota.vel_y
                

            pg.display.flip()
    
    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0,0))
        self.pantalla.blit(self.fondo, (600,0))
        self.pantalla.blit(self.fondo, (0,800))
        self.pantalla.blit(self.fondo, (600,800))

    def crear_muro(self):
        # num filas
        # num columnas
        # bucle filas
        #   bucle columnas
        #       xxxxx <---- trabajar con un solo ladrillo
        filas = 4
        columnas = 5
        margen_superior = 20

        for fila in range(filas):
            for col in range(columnas):
                ladrillo = Ladrillo()
                ancho_muro = ladrillo.rect.width * columnas
                margen_izquierdo = (ANCHO - ancho_muro) / 2
                ladrillo.rect.x = ladrillo.rect.width * col + margen_izquierdo
                ladrillo.rect.y = ladrillo.rect.height * fila + margen_superior
                self.muro.add(ladrillo)

class Mejores_jugadores(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()

        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type or (
                    evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                    return True

            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
