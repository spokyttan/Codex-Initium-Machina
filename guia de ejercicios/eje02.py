print("\n Algoritmo para calculo de sueldo")
print("para calculo de sueldo se debe ingresar sueldo base y ventas realizadas")
try:
    sueldo_base = int(input("Ingrese su sueldo base: "))
    if sueldo_base < 0:
        print("El sueldo no puede ser un numero negativo")
    else:
        i = 1
        while i <= 3:
            ventas = int(input(f"Ahora ingrese la venta {i}: "))
            if ventas < 0:
                print("La venta no puede ser un numero negativo")
            else:
                comision_venta = ventas * 0.1
                print(f"La comision de venta fue: {comision_venta}")
                comision_total = 0
                comision_total = comision_total + comision_venta
                print(comision_total)
                i += 1
        sueldo_final = sueldo_base + comision_total
        print("---------------------------------")
        print("\n Calculo de sueldo finalizado")
        print(f"El sueldo final sera de {sueldo_final}")
        print(f"Con una comision total de {comision_total} tras {i-1} ventas")
except ValueError:
    print("Los numeros ingresados son Invalidos")