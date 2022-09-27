from zooAnimales.animal import Animal


class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(colorPiel="rojo", venenoso=True, habitat="selva", nombre=nombre, edad=edad, genero=genero)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(colorPiel="negro y amarillo", venenoso=False, habitat="selva", nombre=nombre, edad=edad, genero=genero)