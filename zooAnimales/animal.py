class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def movimiento(self):
        return "moving"

    @staticmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.pez import Pez
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"

    def toString(self):
        message = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        if self._zona:
            return f"{message}, la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zona.getZoo().getNombre()}"
        else:
            return message