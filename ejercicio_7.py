#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
#rojos.

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad
    
    def titular(self):
        return self._titular
    
    def cantidad(self):
        return self._cantidad
    
    def setTitular(self, titular):
        self._titular = titular

    def setCantidad(self, cantidad):
        self._cantidad = cantidad
    
    def mostrar(self):
        print(f'El titular: {self.titular()} tiene: {self.cantidad()} cantidad de pesos')

    def ingresar(self,dinero):
        if type(dinero) == int:
            if dinero > 0:
                total = self.cantidad() + dinero
                self.setCantidad(total)
            else:
                print('No puede ingresar números negativos')
        else:
            print('No puede ingresar letras')

    def retirar(self,dinero):
        if type(dinero) == int:
            total = self.cantidad() - dinero
            self.setCantidad(total)
        else:
            print('No puede ingresar letras')

""" cuenta1 = Cuenta('Juan', 5000)

print(cuenta1.cantidad())
print(cuenta1.titular())
cuenta1.mostrar()

cuenta1.ingresar(1000)
cuenta1.mostrar()
cuenta1.retirar(1000)
cuenta1.mostrar() """