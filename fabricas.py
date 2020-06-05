from productos import *

class FabricaAbstracta():
    def crear_izquierda(self): pass
    def crear_derecha(self): pass
    def crear_arriba(self): pass
    def crear_abajo(self): pass

class FabricaSpritesGato(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaGato()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaGato()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaGato()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoGato()
        return abajo.get_sprites()

class FabricaSpritesHulk(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaHulk()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaHulk()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaHulk()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoHulk()
        return abajo.get_sprites()

class FabricaSpritesDragon(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaDragon()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaDragon()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaDragon()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoDragon()
        return abajo.get_sprites()
