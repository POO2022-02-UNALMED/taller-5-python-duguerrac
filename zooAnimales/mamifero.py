from zooAnimales.animal import Animal


class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(pelaje=True, patas=4, habitat="pradera", nombre=nombre, edad=edad, genero=genero)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(pelaje=True, patas=4, habitat="pradera", nombre=nombre, edad=edad, genero=genero)