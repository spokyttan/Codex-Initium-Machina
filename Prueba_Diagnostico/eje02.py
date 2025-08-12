#programa que al ingresar un numero genera la siguinte forma
#1 1
#2 21
#3 321
#4 4321
#..........

n=int(input("ingrese un numero: "))
for i in range (1,n+1):
    for j in range(i,0,-1):
        print(j, end="")
    print()