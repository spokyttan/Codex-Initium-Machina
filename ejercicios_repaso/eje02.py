class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo=titulo
        self.artista=artista
        self.duracion=duracion
    
    def reproducir(self):
        print(f"reproduciendo {self.titulo} de {self.artista}")

    def detener(self):
        print(f"cancion detenida")

    def mostrar_info(self):
        print(f"{self.titulo} de {self.artista}. duracion: {self.duracion}")


spitfire=Cancion("spitfire","skrillex", 3.45)

spitfire.reproducir()

spitfire.detener()

spitfire.mostrar_info()