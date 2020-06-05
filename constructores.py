from fabricas import *
from heroe import *

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeroe(self):
        heroe = Heroe()
        heroe.set_sprites(self.__builder.get_sprites())
        return heroe

class Constructor():
    def get_sprites(self): pass

class ConstructorGato():
    def __init__(self):
        self.fabrica = FabricaSpritesGato()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]

class ConstructorHulk():
    def __init__(self):
        self.fabrica = FabricaSpritesHulk()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]

class ConstructorDragon():
    def __init__(self):
        self.fabrica = FabricaSpritesDragon()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]
