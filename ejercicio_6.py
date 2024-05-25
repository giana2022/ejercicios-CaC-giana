##6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    def setNombre(self, nombre):
        if type(nombre) == str and nombre.isalpha():
            self._nombre = nombre
        else:
            print('Debe ser una cadena de caracteres')
    
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        if type(edad) == int:
            self._edad = edad
        else:
            print('Debe ser un número')
    
    def getEdad(self):
        return self._edad
        
    def setDni(self, dni):
        if type(dni) == int and dni > 99999:
            self._dni = dni
        else:
            print('Debe ser un número')
    
    def getDni(self):
        return self._dni
    
    def Es_mayor_de_edad(self):
        if self.getEdad() > 18:
            print('Es mayor de edad')
        else:
            print('Es menor de edad')

persona1 = Persona('Carlos', 25, 20387964)
print(persona1.getNombre())
print(persona1.getEdad())
print(persona1.getDni())

persona1.setNombre('Juan')
persona1.setEdad(30)
persona1.setDni(44589796)

print(persona1.getNombre())
print(persona1.getEdad())
print(persona1.getDni())

persona1.Es_mayor_de_edad()