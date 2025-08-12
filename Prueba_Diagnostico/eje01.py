# Programa para ingresar números hasta que el usuario escriba 0 y mostrar el mayor
print("Programa para seleccionar el número mayor. Ingrese 0 para terminar.")

primer_numero = True
numeromayor = 0
while True:
    numeroinput = int(input("Ingrese un número (0 para terminar): "))
    if numeroinput == 0:
        break
    if primer_numero:
        numeromayor = numeroinput
        primer_numero = False
    elif numeroinput > numeromayor:
        numeromayor = numeroinput

if not primer_numero:
    print(f"El número mayor es: {numeromayor}")
else:
    print("No se ingresaron números válidos.")