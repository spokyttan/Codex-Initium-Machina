print("Recuerde que si su compra suma en total $1000, se le hara un 20% de descuento")
descuento = 0.2
while True:
    try:
        venta = int(input("Ingrese total a pagar: "))
        if venta > 0:
            print(f"El total a pagar sera {venta}")
            if venta > 1000:
                print("Su venta es valida para el descuento")
                comision_total = venta * descuento
                venta_descuento = venta - comision_total
                print(f"La venta total fue de {venta_descuento}")
                break
        else:
            print("Los datos ingresados deben ser positivos")
    except ValueError:
        print("Los datos ingresados no validos")