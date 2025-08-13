class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca=marca
        self.modelo=modelo
        self.año=año

    def encender(self):
        print(f"El vehiculo {self.marca} {self.modelo} esta encendido")

    def apagar(self):
        print(f"El vehiculo {self.marca} {self.modelo} esta apagado")

    def mostrar_info(self):
        print(f"el vehiculo marca {self.marca}, modelo {self.modelo} del año {self.año}")


auto=Vehiculo("nissan","xlr8",2008)

auto.encender()

auto.apagar()

auto.mostrar_info()