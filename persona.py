class Persona:
    def __init__(self, nombre:str=None, edad:int=None, genero:str=None, direccion:str=None):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

if __name__ == '__main__':
    p1 = Persona(nombre='Karla', genero='M', edad=15, direccion='Norte')
    print(p1)
    print(f'__name__: {__name__}')

