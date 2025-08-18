#La empresa Sitomanboy necesita determinar el sueldo de un empleado, considerando que el valor hora normal es $6.000.- Pesos, la hora extra es un 
#50% mas que la hora normal, existe una cuota del sindicato que depende del sueldo, si es mayor a de 400 Mil se descuenta un 2% del sueldo, de lo contrario 
#un valor fijo es de $3.000 Pesos. Desarrolle el programa que determine el sueldo total de un empleado

sueldo_hora_normal=6000
hora_extra=9000

while True:
    try:
        horas_trabajadas=int(input("Ingrese la cantidad de horas trabajadas: "))
        if horas_trabajadas>40:
            horas_extras=horas_trabajadas-40
            sueldo_normal=40*sueldo_hora_normal
            sueldo_extra=horas_extras*hora_extra
            sueldo_total=sueldo_normal+sueldo_extra
        else:
            sueldo_total=horas_trabajadas*sueldo_hora_normal
        if sueldo_total>400000:
            descuento=sueldo_total*0.02
            sueldo_final=sueldo_total-descuento
        else:
            descuento=3000
            sueldo_final=sueldo_total-descuento
        print("El sueldo total es de:",sueldo_final)
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido para la cantidad de horas trabajadas.")

print("\n--- Desglose del sueldo ---")
print(f"Horas trabajadas: {horas_trabajadas}")
if horas_trabajadas > 40:
    print(f"Horas normales: 40 x ${sueldo_hora_normal} = ${40 * sueldo_hora_normal}")
    print(f"Horas extras: {horas_extras} x ${hora_extra} = ${horas_extras * hora_extra}")
else:
    print(f"Horas normales: {horas_trabajadas} x ${sueldo_hora_normal} = ${horas_trabajadas * sueldo_hora_normal}")
print(f"Sueldo bruto: ${sueldo_total}")
if sueldo_total > 400000:
    print(f"Descuento sindicato (2%): ${descuento}")
else:
    print(f"Descuento sindicato (fijo): ${descuento}")
print(f"Sueldo final: ${sueldo_final}")