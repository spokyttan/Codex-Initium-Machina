"""Ejercicio:
1. Crear una clase Persona con atributos: (rut, nombre, apellido paterno, apellido materno, fechaNacimiento, peso)
2. Método nombrecompleto() que retorne/aparezca un string con apellidos y nombre.
3. Crear una lista de 100 objetos Persona y determinar la edad promedio.
4. Agregar métodos comer() (sube 1 kg) y actividad() (baja 0.1 kg).
5. Cambiar atributo edad por fecha de nacimiento y crear método edad() que calcule la edad real según la fecha actual.

ADICIÓN SOLICITADA:
Se importa el módulo 'random' para generar fechas de nacimiento aleatorias en formato día/mes/año.

EXPLICACIÓN BÁSICA DE 'import random':
El módulo random de la biblioteca estándar de Python permite generar números aleatorios.
Funciones usadas aquí:
 - random.randint(a, b): devuelve un entero entre a y b (INCLUYENDO ambos extremos).
 - random.uniform(a, b): devuelve un número float entre a y b.
 - random.choice(secuencia): devuelve un elemento al azar de una lista/tupla/string.

Para generar una fecha aleatoria completa (día, mes y año) usamos una estrategia mejor que inventar día/mes por separado,
porque algunos meses tienen 30, 31 o 28/29 días. Procedimiento implementado:
 - Definimos una fecha de inicio y una fecha de fin.
 - Calculamos cuántos días hay entre ambas.
 - Elegimos un número aleatorio de días con randint en ese rango.
 - Sumamos ese desplazamiento (timedelta) a la fecha de inicio => obtenemos una fecha válida siempre.

Así evitamos errores como generar 31 de febrero.
"""

import datetime
import random  # <--- Import necesario para generar datos aleatorios (fechas, pesos, etc.)

def generar_fecha_nacimiento(fecha_inicio: datetime.date, fecha_fin: datetime.date) -> datetime.date:
    """Genera y retorna una fecha de nacimiento aleatoria entre fecha_inicio y fecha_fin (incluyendo ambas).

    Parámetros:
        fecha_inicio (datetime.date): límite inferior del rango.
        fecha_fin (datetime.date): límite superior del rango.

    Lógica:
        1. Calcula la diferencia en días entre las dos fechas.
        2. Usa random.randint(0, dias_totales) para obtener un desplazamiento.
        3. Devuelve fecha_inicio + ese desplazamiento.

    Ejemplo rápido:
        >>> generar_fecha_nacimiento(datetime.date(2000,1,1), datetime.date(2005,12,31))
        datetime.date(2003, 7, 14)  # (resultado posible)
    """
    if fecha_fin < fecha_inicio:
        raise ValueError("fecha_fin debe ser mayor o igual que fecha_inicio")
    dias_totales = (fecha_fin - fecha_inicio).days
    desplazamiento = random.randint(0, dias_totales)  # randint incluye ambos extremos
    return fecha_inicio + datetime.timedelta(days=desplazamiento)

class Persona:
    def __init__(self, nombre: str, rut: str, apellidoPaterno: str, apellidoMaterno: str,
                 fechaNacimiento: datetime.date, peso: float):
        self.nombre = nombre
        self.rut = rut
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        # fechaNacimiento ahora es un objeto datetime.date (día, mes, año)
        self.fechaNacimiento = fechaNacimiento
        self.peso = float(peso)

    def nombrecompleto(self) -> str:
        """Retorna el nombre completo en formato: 'ApellidoPaterno ApellidoMaterno, Nombre'."""
        return f"{self.apellidoPaterno} {self.apellidoMaterno}, {self.nombre}"

    def comer(self):
        """Incrementa el peso en 1 kg cada vez que se invoca."""
        self.peso += 1
        print(f"Nuevo peso (comer): {self.peso:.1f} kg")

    def actividad(self):
        """Disminuye el peso en 0.1 kg (simulando actividad física)."""
        self.peso -= 0.1
        print(f"Nuevo peso (actividad): {self.peso:.1f} kg")

    def edad(self) -> int:
        """Calcula y retorna la edad en años completos.

        Fórmula:
            edad = año_actual - año_nacimiento - 1 (si aún no ha llegado el cumpleaños este año)
        """
        hoy = datetime.date.today()
        edad = hoy.year - self.fechaNacimiento.year - (
            (hoy.month, hoy.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day)
        )
        return edad

    def __repr__(self):
        return (f"Persona(nombre={self.nombre!r}, rut={self.rut!r}, apellidos={self.apellidoPaterno!r}/"
                f"{self.apellidoMaterno!r}, fechaNacimiento={self.fechaNacimiento.isoformat()}, peso={self.peso:.1f})")


if __name__ == "__main__":
    # Ejemplo directo de creación de una persona con fecha específica
    persona1 = Persona(
        nombre="Nattan",
        rut="20.497.800-K",
        apellidoPaterno="Chamblat",
        apellidoMaterno="Medel",
        fechaNacimiento=datetime.date(2001, 5, 15),  # día/mes/año
        peso=74
    )

    print("Nombre completo:", persona1.nombrecompleto())
    print("Edad actual:", persona1.edad(), "años")
    persona1.comer()
    persona1.actividad()

    # Ahora generamos 100 personas con datos aleatorios
    lista_personas = []
    fecha_inicio = datetime.date(1980, 1, 1)
    fecha_fin = datetime.date(2015, 12, 31)

    for i in range(100):
        fecha_nac = generar_fecha_nacimiento(fecha_inicio, fecha_fin)
        peso = round(random.uniform(50, 100), 1)  # peso entre 50.0 y 100.0 kg
        rut_random = f"{random.randint(10_000_000, 30_000_000)}-{random.choice('0123456789K')}"
        p = Persona(
            nombre=f"Nombre{i}",
            rut=rut_random,
            apellidoPaterno=f"ApellidoP{i}",
            apellidoMaterno=f"ApellidoM{i}",
            fechaNacimiento=fecha_nac,
            peso=peso
        )
        lista_personas.append(p)

    # Calcular edad promedio
    edades = [p.edad() for p in lista_personas]
    edad_promedio = sum(edades) / len(edades)
    print(f"Se generaron {len(lista_personas)} personas. Edad promedio: {edad_promedio:.2f} años")

    # Mostrar las primeras 5 como muestra
    print("Ejemplos de personas generadas (primeras 5):")
    for p in lista_personas[:5]:
        print(" -", p.nombrecompleto(), "| Fecha nac:", p.fechaNacimiento.strftime("%d/%m/%Y"), "| Edad:", p.edad())

    # Nota: puedes comentar/descomentar impresiones para estudiar el código con calma.