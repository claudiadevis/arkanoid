import os
from random import randint

import pygame as pg

from . import ANCHO, ALTO, VEL_MAX, VEL_MINIMA_Y, VIDAS_INICIALES, TAM_LETRA_MARCADOR, COLOR_OBJETOS


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

    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2
    IMG_LADRILLO = ['greenTile.png', 'redTile.png', 'redTileBreak.png']

    def __init__(self, color = VERDE, puntuacion = 10, fil = 1, columna = 1):
        super().__init__()
        self.puntuacion = puntuacion
        self.ubicacion = [fil, columna]


        self.tipo = color
        self.imagenes = []
        for img in self.IMG_LADRILLO:
            ruta = os.path.join('resources', 'images', img)
            self.imagenes.append(pg.image.load(ruta)) 

        self.image = self.imagenes[color]
        self.rect = self.image.get_rect()

    def update(self, muro):
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
        else: 
            #muro.remove(self)
            #self.remove(muro)
            self.kill()
        self.image = self.imagenes[self.tipo]



class Pelota(pg.sprite.Sprite):

    def __init__(self, raqueta):
        super().__init__()
        self.image =pg.image.load(
            os.path.join('resources', 'images', 'ball1.png')
        )
        self.raqueta = raqueta
        self.init_velocidades()
        self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        self.he_perdido = False

    def update(self, partida_empezada):
        if not partida_empezada:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        else:
            self.rect.x += self.vel_x
            if self.rect.left < 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x

            self.rect.y += self.vel_y
            if self.rect.top < 0:
                self.vel_y = -self.vel_y

            if self.rect.top > ALTO:
                self.he_perdido = True

            #if self.rect.colliderect(self.raqueta):
            #    self.init_velocidades()
            if pg.sprite.collide_mask(self, self.raqueta):
                self.init_velocidades()

    def init_velocidades(self):
        self.vel_x = randint(-VEL_MAX, VEL_MAX)
        self.vel_y = randint(-VEL_MAX, -VEL_MINIMA_Y)

class ContadorVidas:

    def __init__(self, vidas_iniciales, pelota):
        self.vidas_restantes = vidas_iniciales
        self.vidas = [Vida(pelota), Vida(pelota), Vida(pelota)]

    def perder_vida(self):
        self.vidas_restantes -= 1
        self.vidas.pop()
        print('Has perdido una vida. Te quedan', self.vidas_restantes)
        return self.vidas_restantes == 0
    
    def pintar(self, pantalla):
        cont = 0
        for vida in self.vidas:
            vida.pintar_vida(pantalla, cont)
            cont += 1

class Vida():

    def __init__(self, pelota):
        self.image = pelota.image
        self.rect = self.image.get_rect()
        self.ancho = self.rect.width
        self.alto = self.rect.height

    def pintar_vida(self, pantalla, cont):
        margen_izq = 10
        margen_inf = 10
        espacio_entre_pelotas = 5
        x = self.ancho * cont + margen_izq + espacio_entre_pelotas * cont
        y = ALTO - margen_inf - self.alto
        pantalla.blit(self.image, (x, y))


class Marcador():

    nombre_tipo_letra = pg.font.get_default_font()

    def __init__(self):
        self.preparar_tipografia()
        self.reset()

    def preparar_tipografia(self):
        tipos = pg.font.get_fonts()
        letra = 'arial'
        if letra not in tipos:
            letra = pg.font.get_default_font()
        self.tipo_letra = pg.font.SysFont(letra, TAM_LETRA_MARCADOR)
        
    def reset(self):
        self.puntuacion = 0

    def pintame(self, pantalla):
        margen_der = 10
        margen_inf = 10
        img_texto = self.tipo_letra.render(f'Puntos: {self.puntuacion}', True, COLOR_OBJETOS)
        ancho_img = img_texto.get_width()
        alto_img = img_texto.get_height()
        x = ANCHO - margen_der - ancho_img
        y = y = ALTO - margen_inf - alto_img
        pantalla.blit(img_texto,(x,y))

    #def update(self):
    