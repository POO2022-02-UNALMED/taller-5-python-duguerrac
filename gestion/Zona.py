from zooAnimales.Animal import Animal


class Zona:

    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    # set and get
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimaels(self):
        return self._animales

    def setAnimaels(self, animales):
        self._animales = animales

    # Constructores
    def agregarAnimales(self, animal):
        if isinstance(animal, Animal):
            self._animales.append(animal)

    # TENER PRESENTE
    def cantidadAnimales(self):
        return len(self._animales)

    def cantidadTotalAnimales(self):
        return len(self._animales)