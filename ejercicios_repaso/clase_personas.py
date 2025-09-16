import datetime
import random  # <--- Import necesario para generar datos aleatorios (fechas, pesos, etc.)

def generar_fecha_nacimiento(fecha_inicio: datetime.date, fecha_fin: datetime.date) -> datetime.date:
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
        self.fechaNacimiento = fechaNacimiento
        self.peso = float(peso)

    def nombrecompleto(self) -> str:
        return f"{self.apellidoPaterno} {self.apellidoMaterno}, {self.nombre}"

    def comer(self):
        self.peso += 1
        print(f"Nuevo peso (comer): {self.peso:.1f} kg")

    def actividad(self):
        self.peso -= 0.1
        print(f"Nuevo peso (actividad): {self.peso:.1f} kg")

    def edad(self) -> int:
        hoy = datetime.date.today()
        edad = hoy.year - self.fechaNacimiento.year - (
            (hoy.month, hoy.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day)
        )
        return edad

    def __repr__(self):
        return (f"Persona(nombre={self.nombre!r}, rut={self.rut!r}, apellidos={self.apellidoPaterno!r}/"
                f"{self.apellidoMaterno!r}, fechaNacimiento={self.fechaNacimiento.isoformat()}, peso={self.peso:.1f})")


if __name__ == "__main__":
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

    edades = [p.edad() for p in lista_personas]
    edad_promedio = sum(edades) / len(edades)
    print(f"Se generaron {len(lista_personas)} personas. Edad promedio: {edad_promedio:.2f} años")

    print("Ejemplos de personas generadas (primeras 5):")
    for p in lista_personas[:5]:
        print(" -", p.nombrecompleto(), "| Fecha nac:", p.fechaNacimiento.strftime("%d/%m/%Y"), "| Edad:", p.edad())

