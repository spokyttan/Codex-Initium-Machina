#Juanito es muy detallista en todo, y sabe que para lavar N kilos de ropa necesita 300 gramos de detergente y 100 gramos de suavizante, hoy llegó a su 
#casa y ya no le queda ropa limpia, ayúdelo construyendo y programa que calcule cuanto detergente y suavizante debe usar en N Kilos de ropa.
detergente=300
suavizante=100
while True:
    try:
        n=int(input("Ingrese la cantidad de kilos de ropa a lavar: "))
        detergente_total=(n*detergente)
        suavizante_total=(n*suavizante)
        print("Para lavar",n,"kilos de ropa se necesita",detergente_total,"gramos de detergente y",suavizante_total,"gramos de suavizante")
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido para la cantidad de kilos de ropa.")