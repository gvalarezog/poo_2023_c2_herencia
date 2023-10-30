from persona import Persona

class Empleado(Persona):
    contador_empleado = 0
    def __init__(self, nombre:str=None, edad:int=None, genero:str=None, direccion:str=None, sueldo:float=None):
        super().__init__(nombre=nombre, direccion=direccion, edad=edad, genero=genero)
        self._sueldo = sueldo
        Empleado.contador_empleado += 1
        self._idEmpleado = Empleado.contador_empleado

    @property
    def idEmpleado(self):
        return self._idEmpleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: {self.__dict__.__str__()}'


if __name__ == '__main__':
    e1 = Empleado(nombre='Luis', sueldo=450)
    print(e1)
    print(__name__)





