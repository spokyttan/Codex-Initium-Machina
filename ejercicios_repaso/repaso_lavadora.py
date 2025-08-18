detergente = 300
suavizante = 100

while True:
    try:
        n=int(input("Ingrese la cantidad de kilos de ropa a lavar: "))
        detergente_total = (n * detergente)
        suavizante_total = (n * suavizante)
        if detergente_total > 1000:
            detergente_total /= 1000
            print("Para lavar",n,"Kilos de ropa se necesita", detergente_total," kilos de detergente y",suavizante_total,"gramos de suavizante")
            if suavizante_total >= 1000:
                suavizante_total /=1000
                print("Para lavar",n,"Kilos de ropa se necesita", detergente_total," kilos de detergente y",suavizante_total,"kilos de suavizante")
        else:
            print("Para lavar",n,"Kilos de ropa se necesita", detergente_total," gramos de detergente y",suavizante_total,"gramos de suavizante")
        break
    except ValueError:
        print("Ingrese un número entero válido")