from gestion.Zona import Zona


class Zoologico:
    # Atributos
    _zonas = []

    def __init__(self, nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion

    # get and set
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    @classmethod
    def getZona(self):
        return self._zonas

    # Importante
    @classmethod
    def setZona(self, zonas):
        self._zonas = zonas

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @classmethod
    def agregarZonas(cls, zona):
        if isinstance(zona, Zona):
            cls._zonas.append(zona)

    def cantidadTotalAnimales(self):
        cont = 0
        for zona in self._zonas:
            cont += zona.cantidadTotalAnimales()
        return cont