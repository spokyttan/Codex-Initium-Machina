class Libro:
    def __init__(self, titulo,autor, ISBN, estado):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.estado=estado

    #estado={"disponible","prestado"}

    def prestar(self):
        print(f"El libro {self.titulo} de {self.autor} esta {self.estado}")
        if self.estado == "disponible":
            print(f"EL libro se ha solicitado por el usuario.")
            self.estado = "prestado"
            print(f"el libro ha sido entregado, que los disfrutes.")
        else: print(f"el libro esta {self.estado}. No podremos facilitarselo, lo lamentamos")

    def devolver(self):
        print(f"se ha iniciado la devolucion del libro {self.titulo}")
        if self.estado == "prestado":
            self.estado = "disponible"
            print(f"el libro {self.titulo} se ha devuelto con exito")
        else: print(f"ha ocurrido un error con la solicitud")

    def mostrar_info(self):
        print(f"el libro {self.titulo} cuyo autor es {self.autor}, con su ISBN {self.ISBN} esta {self.estado}")


class Usuario:
    def __init__(self,nombre,rut,libros_prestados):
        self.libros_prestados=[]
        self.nombre=nombre
        self.rut=rut

    def tomar_libro(self,libro):
        if libro.estado == "disponible":
            libro.prestar()
            self.libros_prestados.append(libro)
        else:print(f"no se pudo entregar el libro")

    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else: print(f"hubo un problema con la solicitud")