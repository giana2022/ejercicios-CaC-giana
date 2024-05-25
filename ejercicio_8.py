#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#tanto por ciento. Crear los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#mayor de edad pero menor de 25 años y falso en caso contrario.
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
#cuenta.

from ejercicio_7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, edad, bonificacion):
        super().__init__(titular, cantidad)
        self._edad = edad
        self._bonificacion = bonificacion
    
    def edad(self):
        return self._edad

    def bonificacion(self):
        return self._bonificacion
    
    def es_titular_valido(self):
        if self.edad() < 25 and self.edad() > 18:
            print('El titular es válido')
            return True
        else:
            print('El titular no es válido')
            return False

    def retirar(self, dinero):
        if self.es_titular_valido():
            monto = self.cantidad() - dinero
            self.setCantidad(monto)
        else:
            print('El titular no es válido')

    def mostrar(self):
        cuenta_bonif = self.cantidad()+(self.bonificacion() * float(self.cantidad()))
        print(f'El titular: {self.titular()} tiene: {cuenta_bonif} cantidad de pesos')

cuenta2 = CuentaJoven('Juan', 1000, 23, 0.25)
cuenta2.mostrar()
cuenta2.retirar(500)
cuenta2.mostrar()