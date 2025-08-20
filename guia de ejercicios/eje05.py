print("Programa que muestre el porcentaje de hombres y mujeres")
while True:
    try:
        hombres = int(input("Ingrese la cantidad de hombres: "))
        mujeres = int(input("Ingrese la cantidad de mujeres: "))
        if hombres > 0 and mujeres > 0:
            total_alumnos = hombres + mujeres
            print(f"La cantidad total de alumnos es de {total_alumnos} alumnos")
            porcentaje_hombres = int((hombres * 100)/total_alumnos)
            print(f"El porcentaje de hombres es de {porcentaje_hombres}%")
            porcentaje_mujeres = int(100 - porcentaje_hombres)
            print(f"El porcentaje de mujeres es de {porcentaje_mujeres}%")
            break
        else:
            print("La cantidad ingresa debe ser un numero positivo")
    except ValueError:
        print("Los numeros ingresados son invalidos")