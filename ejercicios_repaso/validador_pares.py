#mostrar lista de numeros hasta el numero del usuario, cada numero debe mostrarse a si mismo 
#y si es par o impar

while True:
    try:
        n=int(input("Ingrese un número entero: "))
        for i in range(1,n+1):
            if i % 2 ==0:
                validador= "par"
            else:
                validador="impar"
            print(f"{i} -> {validador}")
    except ValueError:
        print("El número ingresado no es valido")



"""ANDRE:
n = int(input("Ingrese un número: "))

while i <= n:
    if i % 2 == 0:
        print(f"{i} --> par")
    else:
        print(f"{i} --> impar")
        
    i += 1"""

"""fabian:
for i in range (7):

    Num = float(input("ingrese serie de 7 digitos:"))
    par= Num / 2 #numero par
    print(f"{par}--->par")
    impar= Num / 3 #numero impar)
    print(f"{impar} --->impar")
print(f"numeros pares {par}")

print(f"numeros impares {impar} ")"""