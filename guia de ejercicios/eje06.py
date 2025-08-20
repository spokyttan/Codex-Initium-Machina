print("\n ALgoritmo para calcular la edad de una persona")

while True:
    try:
        fecha_nacimiento = int(input("Ingrese su año de nacimiento: "))
        if fecha_nacimiento > 0 :
            año = 2025 - fecha_nacimiento
            print(f"Su fecha de año de nacimiento es {fecha_nacimiento}, por lo tanto si se lo restamos a 2025, el resultaro seria {año} años.")
            break
    except ValueError:
        print("Los datos ingresados son invalidos")