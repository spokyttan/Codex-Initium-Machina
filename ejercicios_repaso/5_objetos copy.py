"""5 Objetos que tengan atributos set y get


"""
"""
5 Objetos del universo Uma Musume: UmaMusume, Carrera, Establo, Habilidad, Equipo
Cada clase tiene atributos privados, getters/setters tradicionales y propiedades Pythonic.
"""

class UmaMusume:
    """Representa a una Uma Musume (chica caballo).
    Atributos:
        _nombre (str): Nombre de la Uma Musume.
        _velocidad (int): Velocidad base.
        _resistencia (int): Resistencia base.
        _habilidad (Habilidad): Habilidad especial.
    """
    def __init__(self, nombre: str, velocidad: int, resistencia: int, habilidad: 'Habilidad') -> None:
        self.set_nombre(nombre)
        self.set_velocidad(velocidad)
        self.set_resistencia(resistencia)
        self.set_habilidad(habilidad)

    def get_nombre(self) -> str:
        return self._nombre
    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self._nombre = nombre.strip().title()

    def get_velocidad(self) -> int:
        return self._velocidad
    def set_velocidad(self, velocidad: int) -> None:
        if not isinstance(velocidad, int) or velocidad < 0:
            raise ValueError("La velocidad debe ser un entero >= 0.")
        self._velocidad = velocidad

    def get_resistencia(self) -> int:
        return self._resistencia
    def set_resistencia(self, resistencia: int) -> None:
        if not isinstance(resistencia, int) or resistencia < 0:
            raise ValueError("La resistencia debe ser un entero >= 0.")
        self._resistencia = resistencia

    def get_habilidad(self) -> 'Habilidad':
        return self._habilidad
    def set_habilidad(self, habilidad: 'Habilidad') -> None:
        if not isinstance(habilidad, Habilidad):
            raise TypeError("habilidad debe ser una instancia de Habilidad.")
        self._habilidad = habilidad

    nombre = property(get_nombre, set_nombre)
    velocidad = property(get_velocidad, set_velocidad)
    resistencia = property(get_resistencia, set_resistencia)
    habilidad = property(get_habilidad, set_habilidad)

    def __repr__(self) -> str:
        return f"UmaMusume(nombre={self._nombre!r}, velocidad={self._velocidad}, resistencia={self._resistencia}, habilidad={self._habilidad.nombre})"


class Habilidad:
    """Habilidad especial de una Uma Musume.
    Atributos:
        _nombre (str): Nombre de la habilidad.
        _descripcion (str): Descripción de la habilidad.
    """
    def __init__(self, nombre: str, descripcion: str) -> None:
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)

    def get_nombre(self) -> str:
        return self._nombre
    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la habilidad no puede ser vacío.")
        self._nombre = nombre.strip().title()

    def get_descripcion(self) -> str:
        return self._descripcion
    def set_descripcion(self, descripcion: str) -> None:
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción no puede ser vacía.")
        self._descripcion = descripcion.strip()

    nombre = property(get_nombre, set_nombre)
    descripcion = property(get_descripcion, set_descripcion)

    def __repr__(self) -> str:
        return f"Habilidad(nombre={self._nombre!r}, descripcion={self._descripcion!r})"


class Establo:
    """Establo donde viven Uma Musume.
    Atributos:
        _nombre (str): Nombre del establo.
        _capacidad (int): Número máximo de Uma Musume.
        _lista_uma (list[UmaMusume]): Uma Musume residentes.
    """
    def __init__(self, nombre: str, capacidad: int) -> None:
        self.set_nombre(nombre)
        self.set_capacidad(capacidad)
        self._lista_uma = []

    def get_nombre(self) -> str:
        return self._nombre
    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del establo no puede ser vacío.")
        self._nombre = nombre.strip().title()

    def get_capacidad(self) -> int:
        return self._capacidad
    def set_capacidad(self, capacidad: int) -> None:
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero > 0.")
        self._capacidad = capacidad

    def get_lista_uma(self) -> list:
        return self._lista_uma

    nombre = property(get_nombre, set_nombre)
    capacidad = property(get_capacidad, set_capacidad)
    lista_uma = property(get_lista_uma)

    def agregar_uma(self, uma: UmaMusume) -> None:
        if not isinstance(uma, UmaMusume):
            raise TypeError("Solo se pueden agregar UmaMusume.")
        if len(self._lista_uma) >= self._capacidad:
            raise ValueError("El establo está lleno.")
        self._lista_uma.append(uma)

    def __repr__(self) -> str:
        return f"Establo(nombre={self._nombre!r}, capacidad={self._capacidad}, residentes={[u.nombre for u in self._lista_uma]})"


class Equipo:
    """Equipo de entrenamiento.
    Atributos:
        _nombre (str): Nombre del equipo.
        _entrenador (str): Nombre del entrenador.
        _miembros (list[UmaMusume]): Uma Musume en el equipo.
    """
    def __init__(self, nombre: str, entrenador: str) -> None:
        self.set_nombre(nombre)
        self.set_entrenador(entrenador)
        self._miembros = []

    def get_nombre(self) -> str:
        return self._nombre
    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del equipo no puede ser vacío.")
        self._nombre = nombre.strip().title()

    def get_entrenador(self) -> str:
        return self._entrenador
    def set_entrenador(self, entrenador: str) -> None:
        if not isinstance(entrenador, str) or not entrenador.strip():
            raise ValueError("El nombre del entrenador no puede ser vacío.")
        self._entrenador = entrenador.strip().title()

    def get_miembros(self) -> list:
        return self._miembros

    nombre = property(get_nombre, set_nombre)
    entrenador = property(get_entrenador, set_entrenador)
    miembros = property(get_miembros)

    def agregar_miembro(self, uma: UmaMusume) -> None:
        if not isinstance(uma, UmaMusume):
            raise TypeError("Solo se pueden agregar UmaMusume.")
        self._miembros.append(uma)

    def __repr__(self) -> str:
        return f"Equipo(nombre={self._nombre!r}, entrenador={self._entrenador!r}, miembros={[u.nombre for u in self._miembros]})"


class Carrera:
    """Carrera entre Uma Musume.
    Atributos:
        _nombre (str): Nombre de la carrera.
        _distancia (int): Distancia en metros.
        _participantes (list[UmaMusume]): Uma Musume que compiten.
    """
    def __init__(self, nombre: str, distancia: int) -> None:
        self.set_nombre(nombre)
        self.set_distancia(distancia)
        self._participantes = []

    def get_nombre(self) -> str:
        return self._nombre
    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la carrera no puede ser vacío.")
        self._nombre = nombre.strip().title()

    def get_distancia(self) -> int:
        return self._distancia
    def set_distancia(self, distancia: int) -> None:
        if not isinstance(distancia, int) or distancia <= 0:
            raise ValueError("La distancia debe ser un entero > 0.")
        self._distancia = distancia

    def get_participantes(self) -> list:
        return self._participantes

    nombre = property(get_nombre, set_nombre)
    distancia = property(get_distancia, set_distancia)
    participantes = property(get_participantes)

    def agregar_participante(self, uma: UmaMusume) -> None:
        if not isinstance(uma, UmaMusume):
            raise TypeError("Solo se pueden agregar UmaMusume.")
        self._participantes.append(uma)

    def __repr__(self) -> str:
        return f"Carrera(nombre={self._nombre!r}, distancia={self._distancia}, participantes={[u.nombre for u in self._participantes]})"


def _demo_uma_musume() -> None:
    print("=== DEMO UMA MUSUME ===")
    hab1 = Habilidad("Speed Star", "Aumenta la velocidad en el sprint final.")
    hab2 = Habilidad("Stamina Up", "Mejora la resistencia en carreras largas.")
    uma1 = UmaMusume("Special Week", 90, 80, hab1)
    uma2 = UmaMusume("Silence Suzuka", 95, 70, hab2)
    est = Establo("Tracen Academy", 10)
    est.agregar_uma(uma1)
    est.agregar_uma(uma2)
    eq = Equipo("Team Spica", "Entrenador")
    eq.agregar_miembro(uma1)
    eq.agregar_miembro(uma2)
    carrera = Carrera("Twinkle Series", 2400)
    carrera.agregar_participante(uma1)
    carrera.agregar_participante(uma2)
    print(uma1)
    print(uma2)
    print(hab1)
    print(est)
    print(eq)
    print(carrera)
    print("=== FIN DEMO ===")

if __name__ == "__main__":
    _demo_uma_musume()
	#_demo_objetos()
