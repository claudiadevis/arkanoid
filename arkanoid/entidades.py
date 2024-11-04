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


