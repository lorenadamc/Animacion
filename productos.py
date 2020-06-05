import util

class Abajo():
    def get_sprites(self): pass

class AbajoGato(Abajo):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Gato/b1.png'),
                util.cargar_imagen('imagenes/Gato/b2.png'),
                util.cargar_imagen('imagenes/Gato/b3.png'),
                util.cargar_imagen('imagenes/Gato/b4.png')]

class AbajoHulk(Abajo):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Hulk/b1.png'),
                util.cargar_imagen('imagenes/Hulk/b2.png'),
                util.cargar_imagen('imagenes/Hulk/b3.png'),
                util.cargar_imagen('imagenes/Hulk/b4.png')]

class AbajoDragon(Abajo):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Dragon/b1.png'),
                util.cargar_imagen('imagenes/Dragon/b2.png'),
                util.cargar_imagen('imagenes/Dragon/b3.png'),
                util.cargar_imagen('imagenes/Dragon/b4.png')]

class Arriba():
    def get_sprites(self): pass

class ArribaGato(Arriba):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Gato/a1.png'),
                util.cargar_imagen('imagenes/Gato/a2.png'),
                util.cargar_imagen('imagenes/Gato/a3.png'),
                util.cargar_imagen('imagenes/Gato/a4.png')]

class ArribaHulk(Arriba):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Hulk/a1.png'),
                util.cargar_imagen('imagenes/Hulk/a2.png'),
                util.cargar_imagen('imagenes/Hulk/a3.png'),
                util.cargar_imagen('imagenes/Hulk/a4.png')]

class ArribaDragon(Arriba):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Dragon/a1.png'),
                util.cargar_imagen('imagenes/Dragon/a2.png'),
                util.cargar_imagen('imagenes/Dragon/a3.png'),
                util.cargar_imagen('imagenes/Dragon/a4.png')]

class Derecha():
    def get_sprites(self): pass

class DerechaGato(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Gato/d1.png'),
                util.cargar_imagen('imagenes/Gato/d2.png'),
                util.cargar_imagen('imagenes/Gato/d3.png'),
                util.cargar_imagen('imagenes/Gato/d4.png')]

class DerechaHulk(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Hulk/d1.png'),
                util.cargar_imagen('imagenes/Hulk/d2.png'),
                util.cargar_imagen('imagenes/Hulk/d3.png'),
                util.cargar_imagen('imagenes/Hulk/d4.png')]

class DerechaDragon(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Dragon/d1.png'),
                util.cargar_imagen('imagenes/Dragon/d2.png'),
                util.cargar_imagen('imagenes/Dragon/d3.png'),
                util.cargar_imagen('imagenes/Dragon/d4.png')]

class Izquierda():
    def get_sprites(self): pass

class IzquierdaGato(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Gato/i1.png'),
                util.cargar_imagen('imagenes/Gato/i2.png'),
                util.cargar_imagen('imagenes/Gato/i3.png'),
                util.cargar_imagen('imagenes/Gato/i4.png')]

class IzquierdaHulk(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Hulk/i1.png'),
                util.cargar_imagen('imagenes/Hulk/i2.png'),
                util.cargar_imagen('imagenes/Hulk/i3.png'),
                util.cargar_imagen('imagenes/Hulk/i4.png')]

class IzquierdaDragon(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/Dragon/i1.png'),
                util.cargar_imagen('imagenes/Dragon/i2.png'),
                util.cargar_imagen('imagenes/Dragon/i3.png'),
                util.cargar_imagen('imagenes/Dragon/i4.png')]
