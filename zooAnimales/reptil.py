from zooAnimales.animal import Animal


class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(colorEscamas="verde", largoCola=3, habitat="humedal", nombre=nombre, edad=edad, genero=genero)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(colorEscamas="blanco", largoCola=1, habitat="jungla", nombre=nombre, edad=edad, genero=genero)