#1. Escribir una función que calcule el máximo común divisor entre dos números.
def minComunDivisor(a, b):
    while b:
        a, b = b, a % b
    return a

numer1 = 48
numer2 = 18
mcdiv = minComunDivisor(numer1, numer2)
print(f"El MCD de {numer1} y {numer2} es {mcdiv}")

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def minimoComunMultiplo(n1, n2):
    x = None
    multiplo = 1
    lista_n = []
    a_comparar = None
    if n1 > n2:
        a_comparar = n1
        comparador = n2
    else:
        a_comparar = n2
        comparador = n1
    while x == None:
        lista_n.append(a_comparar * multiplo)
        mulpl_segundo = comparador * multiplo
        if mulpl_segundo in lista_n:
            x = mulpl_segundo
            break
        multiplo += 1
    return x

print(minimoComunMultiplo(2,3))
    
#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def cadena_Dict(palabra):
    diccionario = {}
    cadena = ''
    for c in palabra:
        if c != ',' and c != '.' and c != '-':
            cadena += c
    lista_cadena = cadena.split()
    for palabra in lista_cadena:
        if palabra not in diccionario.keys():
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
    return diccionario

frase = 'Un múltiplo común es un número que es múltiplo a la vez de dos o más números, es decir, es un múltiplo común a esos números.'
dic = cadena_Dict(frase)
print(dic)

#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.
def cadena_Dict2(palabra):
    diccionario = {}
    cadena = ''
    for c in palabra:
        if c != ',' and c != '.' and c != '-':
            cadena += c
    lista_cadena = cadena.split()
    for palabra in lista_cadena:
        if palabra not in diccionario.keys():
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
    return diccionario

def tuplaDict(dic):
    mas_frecuente = None
    for k,v in dic.items():
        if mas_frecuente == None:
            mas_frecuente = [k,v]
        else:
            if v > mas_frecuente[1]:
                mas_frecuente = [k,v]
    return tuple(mas_frecuente)
        

frase = 'Un múltiplo común es un número que es múltiplo a la vez de dos o más números, es decir, es un múltiplo común a esos números.'
dic = cadena_Dict2(frase)
print(tuplaDict(dic))

#5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva. 
def getint_iterativo():
  valor = None
  while valor == None:
    try:
        valor = int(input("Ingrese un número entero: "))
        return valor 
    except ValueError:
        valor == None
        print("Error. Valor inválido")

def getint_recursivo():
  try:
        valor = int(input("Ingrese un número entero: "))
        return valor
  except ValueError:
        print("Error. Valor inválido")
        return getint_recursivo() 


##6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

