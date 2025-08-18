"""desarrolle un programa que permita ingresar 3 numeros y despliegue el mayor
(siempre el usuario va ingresar numeros distintos y  sin ciclo)"""

while True:
    try:
        n = int(input("Ingrese el primer número: "))
        numero_mayor = n
        print(numero_mayor)
        n = int(input("Ingrese el segundo número: "))
        if n > numero_mayor:
            numero_mayor = n
        print(numero_mayor)
        n = int(input("Ingrese el tercer número: "))
        if n > numero_mayor:
            numero_mayor = n
        print(numero_mayor)
    except ValueError:
        print("Ingrese un número valido")

"""profesor:
numA = int(input("Ingresa 1er número: "))
numB = int(input("Ingresa 2do número: "))
numC = int(input("Ingresa 3er número: "))

if numA > numB and numA > numC:
    print(numA)
else:
    if numB > numC:
        print(numB)
    else:
        print(numC)"""