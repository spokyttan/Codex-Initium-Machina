class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print(f"titulo: {self.titulo}, autor: {self.autor} y año de publicacion: {self.anio}")


leviathan=Libro("leviathan","tiranidos",41999)

leviathan.mostrar_info()

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.anio}")

# Crear objeto
leviathan = Libro("Leviathan", "Tiranidos", 41999)

# Mostrar información
leviathan.mostrar_info()
