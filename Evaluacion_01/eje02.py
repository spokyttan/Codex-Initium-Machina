numero = int(input("Ingrese un numero para crear secuencia: "))

lista_numeros = []
nueva_lista = []
i = 1
while i <= numero:
    lista_numeros.append(i)
    nueva_lista.extend([i]*i)
    i += 1

print(nueva_lista)