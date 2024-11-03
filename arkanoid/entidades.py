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
        ruta_img = os.path.join('resources', 'images', 'electric00.png')
        self.image = pg.image.load(ruta_img)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-25))

    def pintar(self):
        pass


