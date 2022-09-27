from zooAnimales.animal import Animal


class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        return "flying"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        return Ave(colorPlumas="cafe glorioso", habitat="montanas", nombre=nombre, edad=edad, genero=genero)

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(colorPlumas="blanco y amarillo", habitat="montanas", nombre=nombre, edad=edad, genero=genero)