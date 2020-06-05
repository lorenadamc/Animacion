import sys
import pygame
import util
from pygame.locals import *
from constructores import *
import copy
SCREEN_WIDTH = 626
SCREEN_HEIGHT = 417
def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Animación")
    inicio_image = util.cargar_imagen('imagenes/inicio.png')
    screen.blit(inicio_image, (0, 0))
    pygame.mouse.set_visible(False)
    jugando = False
    elegido= False
    ejecutando = True
    director = Director()
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        teclas = pygame.key.get_pressed()
        if teclas[K_g]:
            background_image = util.cargar_imagen('imagenes/Gato/fondo.gif')
            director.setBuilder(ConstructorGato())
            elegido = True
        if teclas[K_h]:
            background_image = util.cargar_imagen('imagenes/Hulk/fondo.gif')
            director.setBuilder(ConstructorHulk())
            elegido = True
        if teclas[K_d]:
            background_image = util.cargar_imagen('imagenes/Dragon/fondo.gif')
            director.setBuilder(ConstructorDragon())
            elegido = True
        if teclas[K_SPACE] and elegido:
            heroe = director.getHeroe()
            heroe.ubicar((350, 120))
            jugando = True
        if jugando:
            screen.blit(background_image, (0, 0))
            heroe.update()
            heroe.draw(screen)
        if teclas[K_ESCAPE]:
            ejecutando = False
            sys.exit()
        pygame.display.update()
        pygame.time.delay(10)
if __name__ == '__main__':
    game()
