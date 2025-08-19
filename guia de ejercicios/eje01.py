print("\n Algoritmo para calcular ganancia mensual")
try:
    n = int(input("Ingrese la cantidad de dinero a invertir: "))
    if n < 0:
        print("No se puede invertir con un número negativo")
    else:
        inversion = n * 0.02
        inversion_total = n + inversion
        print(f"Si ustedes ingresa {n}, la cantidad que genera al mes es {inversion}, lo cual en total serian {inversion_total} al mes ")

except ValueError:
    print("Ingrese un numero valido")
