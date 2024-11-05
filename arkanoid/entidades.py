import os

import pygame as pg

from . import ANCHO, ALTO


class Raqueta(pg.sprite.Sprite):
    """
    1. Es un tipo Sprite (usar herencia)
    2. Se puede mover (método)
    3. Pintar en pantalla (método)
    4. Volver a la posición inicial
    5....
    """

    velocidad = 10

    #Sprite permite coger una imagen y pintarla como objeto, el sprite es el hueco donde 
    #se va a encajar la imagen

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            ruta_img = os.path.join('resources', 'images', f'electric0{i}.png')
            img = pg.image.load(ruta_img)
            self.imagenes.append(img)

        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-25))

    def update(self):
        #00 -> 01 -> 02 -> 00 -> 01
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]

        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0
        if teclas_pulsadas[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO


class Ladrillo(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        ruta_verde = os.path.join('resources', 'images', 'greenTile.png')
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()

    def update(self):
        pass



class Pelota(pg.sprite.Sprite):

    vel_y = -10
    vel_x = -13

    def __init__(self, raqueta):
        super().__init__()
        self.image =pg.image.load(
            os.path.join('resources', 'images', 'ball1.png')
        )
        self.raqueta = raqueta

    def update(self, partida_empezada):
        if not partida_empezada:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
        