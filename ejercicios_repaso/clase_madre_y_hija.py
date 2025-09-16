class Tecnosacerdote:
    """Representa a un Tecnosacerdote del Adeptus Mechanicus.

    Atributos:
        nombre (str): Identificador o nombre de la unidad / sacerdote.
        rango (str): Rango dentro de la jerarquía (ej: 'Magos Dominus').
        especialidad (str): Área de conocimiento o liturgia principal.
    """

    def __init__(self, nombre: str, rango: str, especialidad: str) -> None:
        """Inicializa un Tecnosacerdote.

        Args:
            nombre: Nombre o código del tecnosacerdote.
            rango: Rango jerárquico.
            especialidad: Campo de especialización litúrgica.
        """
        self.nombre: str = nombre
        self.rango: str = rango
        self.especialidad: str = especialidad

    def recitar_liturgia(self) -> str:
        """Construye y retorna la frase de recitación litúrgica.

        Returns:
            str: Texto de la liturgia recitada.
        """
        liturgia = f"{self.rango} {self.nombre} recita la liturgia de la {self.especialidad}"
        return liturgia

    def bendecir_maquina(self, nombre_maquina: str) -> str:
        """Genera una bendición para una máquina.

        Args:
            nombre_maquina: Nombre o identificador de la máquina.

        Returns:
            str: Fórmula de bendición.
        """
        return (f"{self.rango} {self.nombre} entona binarios sagrados para la máquina {nombre_maquina}. "
                f"Que la {self.especialidad} preserve sus engranajes.")

    def actualizar_especialidad(self, nueva_especialidad: str) -> None:
        """Actualiza la especialidad del Tecnosacerdote.

        Args:
            nueva_especialidad: Nuevo campo de especialización.
        """
        self.especialidad = nueva_especialidad

    def calibrar_componentes(self, *componentes: str) -> str:
        """Simula la calibración de uno o más componentes.

        Args:
            *componentes: Lista variable de nombres de componentes.

        Returns:
            str: Resumen de calibración.
        """
        if not componentes:
            return "No se proporcionaron componentes para calibrar."
        listado = ", ".join(componentes)
        return (f"{self.nombre} ejecuta protocolo de calibración sobre: {listado}. "
                f"Ajustes aplicados según doctrina {self.especialidad}.")

    @property
    def identificador(self) -> str:
        """Retorna un identificador compuesto del tecnosacerdote."""
        return f"{self.rango}-{self.nombre}-{self.especialidad.replace(' ', '_')}"

    def __repr__(self) -> str:  # Representación útil para depuración
        return (f"Tecnosacerdote(nombre={self.nombre!r}, rango={self.rango!r}, "
                f"especialidad={self.especialidad!r})")
    
class Servocraneo(Tecnosacerdote):
    """Servocráneo asistente que hereda parámetros básicos de un Tecnosacerdote.

    Atributos adicionales:
        funcion (str): Rol específico de asistencia.
        nivel_de_pureza (float): Métrica de pureza de código / datos (%).
    """

    def __init__(self, nombre: str, rango: str, especialidad: str, funcion: str, nivel_de_pureza: float) -> None:
        """Inicializa el Servocráneo.

        Args:
            nombre: Identificador o código.
            rango: Rango asociado (puede replicar el del tecnosacerdote maestro).
            especialidad: Especialidad heredada.
            funcion: Función principal de asistencia.
            nivel_de_pureza: Porcentaje de pureza (0 - 100).
        """
        super().__init__(nombre, rango, especialidad)
        self.funcion: str = funcion
        self.nivel_de_pureza: float = nivel_de_pureza

    def ejecutar_funcion(self) -> str:
        """Ejecuta la función asignada y retorna un reporte textual.

        Returns:
            str: Mensaje con la función y pureza actual.
        """
        ejecucion = f"Servocraneo ejecutando funcion: {self.funcion} con una pureza de codigo nivel {self.nivel_de_pureza}%"
        return ejecucion

    def escanear(self, objetivo: str) -> str:
        """Simula un escaneo del entorno u objeto.

        Args:
            objetivo: Elemento a escanear.

        Returns:
            str: Resultado del escaneo.
        """
        return (f"Servocraneo {self.nombre} escanea {objetivo}. "
                f"Pureza de algoritmos: {self.nivel_de_pureza}%.")

    def reporte_diagnostico(self) -> str:
        """Genera un reporte de diagnóstico breve del servocráneo.

        Returns:
            str: Texto del diagnóstico.
        """
        estado = "OPTIMO" if self.nivel_de_pureza >= 95 else "DEGRADADO"
        return (f"[DIAGNOSTICO] Funcion={self.funcion} | Pureza={self.nivel_de_pureza}% | Estado={estado}")

    def actualizar_pureza(self, delta: float) -> float:
        """Ajusta la pureza en un delta positivo o negativo.

        Args:
            delta: Variación a aplicar (puede ser negativa).

        Returns:
            float: Nuevo nivel de pureza limitado a 0-100.
        """
        self.nivel_de_pureza = max(0.0, min(100.0, self.nivel_de_pureza + delta))
        return self.nivel_de_pureza

    def recitar_liturgia(self) -> str:  # Override opcional con matiz
        """Extiende la liturgia agregando mención a su función asignada."""
        base = super().recitar_liturgia()
        return base + f" mientras asiste en '{self.funcion}'"

    def __repr__(self) -> str:
        return (f"Servocraneo(nombre={self.nombre!r}, rango={self.rango!r}, "
                f"especialidad={self.especialidad!r}, funcion={self.funcion!r}, "
                f"nivel_de_pureza={self.nivel_de_pureza!r})")
    
magos = Tecnosacerdote("CR-42","Magos Dominus","Mecanica Sagrada")
unidad = Servocraneo("CR-42","Magos Dominus","Mecanica Sagrada","Asistencia academica",99.9)

if __name__ == "__main__":
    # Ejemplos de uso básico
    print(magos.recitar_liturgia())
    print(unidad.ejecutar_funcion())
    print(magos.bendecir_maquina("Reactor Plasma A-17"))
    print(magos.calibrar_componentes("ServoBrazo", "Sensor Óptico"))
    print("Identificador magos:", magos.identificador)

    # Uso de métodos del Servocráneo
    print(unidad.escanear("Terminal Data"))
    print(unidad.reporte_diagnostico())
    unidad.actualizar_pureza(-10.5)
    print(unidad.reporte_diagnostico())
    print(unidad.recitar_liturgia())

    # Mostrar representaciones
    print(repr(magos))
    print(repr(unidad))