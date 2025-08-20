print("\n Algoritmo para calcular inversion")

while True:
    try:
        monto_invertir = int(input("Ingrese el monto total a invertir: "))
        tiempo_inversion = int(input("Ahora ingrese el tiempo en meses de la inversion: "))
        intereses = int(input("Por ultimo, ingrese el porcentaje de interes mensual: "))
        if monto_invertir > 0 and tiempo_inversion > 0 and intereses > 0:
            intereses_procesados = float(intereses/100)
            calculo = (monto_invertir * intereses_procesados)*tiempo_inversion
            if calculo >= 7000:
                print("Los intereses generados se reinvertiran")
                monto_final = monto_invertir + calculo
                print(F"El monto total de inversion serian {monto_final} pesos")
            else:
                print(f"Los intereses totales serian de {calculo}")
    except ValueError:
        print("Los caracteres ingresados no son validos")