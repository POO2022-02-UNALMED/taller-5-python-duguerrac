class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitad, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitad = habitad
        self._genero = genero
        self._zona = None
        self._totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitad

    def setHabitat(self, habitad):
        self._habitad = habitad

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    def toString(self):
        if self._zona:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitad} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zona.getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitad} y mi genero es {self._genero}"

    @classmethod
    def totalPorTipo(self):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.CantidadAnfibio()}"

    def cantidadAnimales(self):
        return len(self._animales)