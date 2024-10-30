from arkanoid.game import Arkanoid
import arkanoid


if __name__ == '__main__':
    print('Arrancamos el juego desde main.py')
    print(f'La pantalla tiene un tamaño de ({arkanoid.ANCHO}, {arkanoid.ALTO})')
    juego = Arkanoid()
    juego.jugar()