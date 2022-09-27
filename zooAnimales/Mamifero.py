from zooAnimales.animal import Animal


class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    def getListado(self):
        return self._listado

    def getCaballos(self):
        return self._caballos

    def getLeones(self):
        return self._leones

    def getPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    def setListado(self, listado):
        self._listado = listado

    def setCaballos(self, caballos):
        self._caballos = caballos

    def setLeones(self, leones):
        self._leones = leones

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def setPatas(self, patas):
        self._patas = patas

    def isPelaje(self):
        return self._pelaje

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, lis):
        cls._listado = lis