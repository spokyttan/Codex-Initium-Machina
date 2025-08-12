#programa para ingresar un numero y revisar si es un numero perfecto

n=int(input("ingrese un numero para verificar si es un numero perfecto: "))
suma=0
for i in range(1,n):
    if n % i ==0:
        suma+=i
if suma==n:
    print("el numero",n,"es perfecto")
else:
    print("numero",n,"no es perfecto")