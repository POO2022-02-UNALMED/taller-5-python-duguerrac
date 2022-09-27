from zooAnimales.animal import Animal


class Anfibio(Animal):
    # ATRIBUTOS
    ranas = 0
    salamandras = 0
    _listado = []

    # CONSTRUCTOR
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    @classmethod
    def CantidadAnfibio(cls):
        return len(cls._listado)

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, lis):
        cls._listado = lis

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso