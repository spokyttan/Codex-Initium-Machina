while True:
    try:
        i=1
        notas = []
        while i <= 10:
            nota = float(input(f"Ingrese la nota {i}: "))
            if nota >= 1.0 and nota < 7.1:
                notas.append(nota)
                i+=1
            else:
                print("ingrese una nota valida")
        promedio = sum(notas)/len(notas)
        print(f"El promedio de las notas ingresadas {promedio}")
        notas = [nota for nota in notas if nota >= promedio]
        print(notas)
        break
    except ValueError:
            print("ingrese un numero valido")