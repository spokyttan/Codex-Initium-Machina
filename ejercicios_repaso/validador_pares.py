#mostrar lista de numeros hasta el numero del usuario, cada numero debe mostrarse a si mismo 
#y si es par o impar

def es_Par(numero):
        if numero % 2 == 0:
            return True
        else:
            return False


while True:
    try:
        n = int(input("Ingrese un número: "))
        for i in range(1,n+1):
            if es_Par(i):
                 print(F"{i} -> Es par")
            else:
                 print(f"{i} -> Es impar")
    except ValueError:
        print("Número invalido")


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
