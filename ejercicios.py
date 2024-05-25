#1. Escribir una función que calcule el máximo común divisor entre dos números.
def minComunDivisor(a, b):
    while b:
        a, b = b, a % b
    return a

numer1 = 48
numer2 = 18
mcd = minComunDivisor(numer1, numer2)
print(f"El MCD de {numer1} y {numer2} es {mcd}")

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

