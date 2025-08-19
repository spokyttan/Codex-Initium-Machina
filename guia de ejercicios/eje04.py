dicc_notas = {}
primera_nota = 0.55
segunda_nota = 0.3
tercera_nota = 0.15

print("Algoritmo para promedio final")

promedio_calificaciones = float(input("Ingrese el promedio de sus 3 calificaciones parciales: "))
examen_final = float(input("Ahora ingrese la calificacion de su examen final: "))
trabajo_final = float(input("Por ultimo, ingrese la calificacion de su trabajo final: "))

print("\n Sus notas ingresadas fueron: ")
print(f"Promedio de sus 3 calificaciones es {promedio_calificaciones}, su nota de examen final fue {examen_final} y la calificacion del trabajo final fue {trabajo_final}")
promedio_final = int((promedio_calificaciones * primera_nota + examen_final * segunda_nota + trabajo_final * tercera_nota) * 10) / 10
print(f"Lo cual nos de su promedio final, que es {promedio_final}")