while True:
    try:
        i = 1
        suma_notas = 0
        while i <= 3:
            nota = float(input(f"Ingrese la nota {i}: "))
            if nota >= 1.0 and nota < 7.1:
                suma_notas = suma_notas + nota
                i += 1
            else:
                print("Nota igresada no es valida")
        promedio = suma_notas/3
        if promedio > 69:
            print(f"El alumno esta Aprobado con un promedio final de {promedio}")
        else:
            print(f"El alumno no aprobo, su promedio fue de {promedio} ")
        break
    except ValueError:
        print("Ingrese valores validos")