from datetime import datetime

class Dueno:
    def __init__(self, run, nombre, apellido, telefono):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def listar_mascotas(self):
        return [mascota.nombre for mascota in self.mascotas]

class Mascota:
    def __init__(self, identificador, nombre, edad, alergico, tipo, dueno):
        self.identificador = identificador
        self._nombre = nombre
        self.edad = edad
        self.alergico = alergico
        self.tipo = tipo
        self.dueno = dueno
        self.atenciones = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    def agregar_atencion(self, atencion):
        self.atenciones.append(atencion)

    def mostrar_info(self):
        print(f"Mascota: {self.nombre} {self.tipo}, Edad: {self.edad}, Alergico: {'Sí' if self.alergico else 'No'}, Dueño: {self.dueno.nombre_completo()}")

class Medico:
    def __init__(self, run, nombre, apellido, anos_trabajados):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.anos_trabajados = anos_trabajados

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Atencion:
    def __init__(self, fecha, medico, diagnostico, prescripcion):
        self.fecha = fecha
        self.medico = medico
        self.diagnostico = diagnostico
        self.prescripcion = prescripcion

    def mostrar_detalle(self):
        print(f"{self.fecha.strftime('%d/%m/%Y')} - Médico: {self.medico.nombre_completo()}, Diagnóstico: {self.diagnostico}, Prescripción: {self.prescripcion}")


if __name__ == "__main__":
    dueno1 = Dueno("12.345.678-9", "Juan", "Pérez", "987654321")
    medico1 = Medico("11.111.111-1", "ana", "gomez", "945464173")

    mascota1 = Mascota("001", "Firulais", 3, False, "Perro", dueno1)
    dueno1.agregar_mascota(mascota1)

    atencion1 = Atencion(datetime.now(), medico1, "Resfriado", "Antibioticos y reposo")
    mascota1.agregar_atencion(atencion1)

    mascota1.mostrar_info()
    print("Atenciones:")
    atencion1.mostrar_detalle()