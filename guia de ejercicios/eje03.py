while True:
    try:
        pago = int(input("Ingrese el total de pago: "))
        if pago > 0:
            descuento = 0.15
            pago_descuento = pago * descuento
            pago_total = pago - pago_descuento
            print(F"El descuento es de {pago_descuento}")
            print(f"el pago total es de {pago_total} pesos chilenos")
            break
        else:
            print("Erro: el numero ingresado es negativo")
    except ValueError:
        print("Error: el digito ingreado no es valido")