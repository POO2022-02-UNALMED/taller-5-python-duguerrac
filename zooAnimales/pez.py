from zooAnimales.animal import Animal


class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(colorEscamas="rojo", cantidadAletas=6, habitat="oceano", nombre=nombre, edad=edad, genero=genero)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(colorEscamas="gris", cantidadAletas=6, habitat="oceano", nombre=nombre, edad=edad, genero=genero)