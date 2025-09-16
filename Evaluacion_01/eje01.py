"""I.	Desarrolle un programa que permita ingresar una frase y la despliegue de forma inversa
No usar método reverse.
Por ej. 

Ingrese frase : programar es muy fácil
Fácil muy es programar
"""


frase = input("Ingrese una frase para devolverla al reves: ")
palabra = frase.split()
frase_final = []
for i in range(len(palabra)-1, -1, -1):
    frase_final.append(palabra[i])
    print(palabra[i], end=" ")