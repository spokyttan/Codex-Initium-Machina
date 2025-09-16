"""5 Objetos que tengan atributos set y get

Este archivo implementa 5 clases (objetos) de ejemplo, cada una con:
 - Atributos "privados" (convención guion bajo: _atributo)
 - Métodos get_<atributo>() y set_<atributo>() al estilo tradicional (como suele pedirse en tareas)
 - Adicionalmente, propiedades Python (@property) para mostrar la forma *pythonic* moderna
 - Validaciones básicas dentro de los setters para asegurar integridad de datos

CLASES:
 1. Persona         -> nombre, edad
 2. CuentaBancaria  -> titular, saldo
 3. Producto        -> codigo, nombre, precio
 4. Libro           -> titulo, autor, paginas
 5. Vehiculo        -> marca, modelo, anio, velocidad

Al final hay un bloque de demostración protegido con if __name__ == "__main__":
Se crean instancias, se usan getters/setters y se muestran resultados.

NOTA SOBRE ESTILO:
En Python moderno se prefiere usar @property en lugar de get_/set_. Sin embargo, como la
instrucción de la tarea pide explícitamente "atributos set y get", se incluyen ambos enfoques.
Puedes usar cualquiera según lo que pida tu profesor(a).
"""

from __future__ import annotations


class Persona:
	"""Representa a una persona con nombre y edad.

	Atributos:
		_nombre (str): Nombre de la persona.
		_edad (int): Edad en años, debe ser >= 0.
	"""

	def __init__(self, nombre: str, edad: int) -> None:
		# Usamos los setters para reutilizar validaciones
		self.set_nombre(nombre)
		self.set_edad(edad)

	# --- Métodos estilo tradicional ---
	def get_nombre(self) -> str:
		return self._nombre

	def set_nombre(self, nombre: str) -> None:
		if not isinstance(nombre, str) or not nombre.strip():
			raise ValueError("El nombre debe ser un texto no vacío.")
		self._nombre = nombre.strip().title()

	def get_edad(self) -> int:
		return self._edad

	def set_edad(self, edad: int) -> None:
		if not isinstance(edad, int) or edad < 0:
			raise ValueError("La edad debe ser un entero >= 0.")
		self._edad = edad

	# --- Versión Pythonic con @property ---
	nombre = property(get_nombre, set_nombre, doc="Nombre de la persona.")
	edad = property(get_edad, set_edad, doc="Edad (entero >= 0).")

	def __repr__(self) -> str:  # Representación útil para debug
		return f"Persona(nombre={self._nombre!r}, edad={self._edad})"


class CuentaBancaria:
	"""Cuenta bancaria simple con titular y saldo.

	Atributos:
		_titular (Persona | str): Titular de la cuenta (acepta str o Persona).
		_saldo (float): Saldo no negativo.
	"""

	def __init__(self, titular: Persona | str, saldo: float = 0.0) -> None:
		self.set_titular(titular)
		self.set_saldo(saldo)

	def get_titular(self) -> Persona | str:
		return self._titular

	def set_titular(self, titular: Persona | str) -> None:
		if isinstance(titular, str):
			if not titular.strip():
				raise ValueError("El titular (str) no puede ser vacío.")
			self._titular = titular.strip().title()
		elif isinstance(titular, Persona):
			self._titular = titular
		else:
			raise TypeError("Titular debe ser str o Persona.")

	def get_saldo(self) -> float:
		return self._saldo

	def set_saldo(self, saldo: float) -> None:
		if not isinstance(saldo, (int, float)) or saldo < 0:
			raise ValueError("El saldo debe ser numérico y >= 0.")
		self._saldo = float(saldo)

	titular = property(get_titular, set_titular, doc="Titular de la cuenta.")
	saldo = property(get_saldo, set_saldo, doc="Saldo disponible (float >= 0).")

	# Métodos adicionales de negocio
	def depositar(self, monto: float) -> None:
		if monto <= 0:
			raise ValueError("El monto a depositar debe ser > 0.")
		self._saldo += monto

	def girar(self, monto: float) -> None:
		if monto <= 0:
			raise ValueError("El monto a girar debe ser > 0.")
		if monto > self._saldo:
			raise ValueError("Fondos insuficientes.")
		self._saldo -= monto

	def __repr__(self) -> str:
		return f"CuentaBancaria(titular={self._titular!r}, saldo={self._saldo:.2f})"


class Producto:
	"""Producto de inventario.

	Atributos:
		_codigo (str): Código único del producto.
		_nombre (str): Nombre descriptivo.
		_precio (float): Precio > 0.
	"""

	def __init__(self, codigo: str, nombre: str, precio: float) -> None:
		self.set_codigo(codigo)
		self.set_nombre(nombre)
		self.set_precio(precio)

	def get_codigo(self) -> str:
		return self._codigo

	def set_codigo(self, codigo: str) -> None:
		if not isinstance(codigo, str) or not codigo.strip():
			raise ValueError("El código debe ser un string no vacío.")
		self._codigo = codigo.strip().upper()

	def get_nombre(self) -> str:  # type: ignore[override]
		return self._nombre

	def set_nombre(self, nombre: str) -> None:  # type: ignore[override]
		if not isinstance(nombre, str) or not nombre.strip():
			raise ValueError("El nombre del producto no puede ser vacío.")
		self._nombre = nombre.strip().title()

	def get_precio(self) -> float:
		return self._precio

	def set_precio(self, precio: float) -> None:
		if not isinstance(precio, (int, float)) or precio <= 0:
			raise ValueError("El precio debe ser numérico y > 0.")
		self._precio = float(precio)

	codigo = property(get_codigo, set_codigo, doc="Código del producto.")
	nombre = property(get_nombre, set_nombre, doc="Nombre del producto.")
	precio = property(get_precio, set_precio, doc="Precio (> 0).")

	def __repr__(self) -> str:
		return f"Producto(codigo={self._codigo!r}, nombre={self._nombre!r}, precio={self._precio:.2f})"


class Libro:
	"""Representa un libro.

	Atributos:
		_titulo (str)
		_autor (str)
		_paginas (int) > 0
	"""

	def __init__(self, titulo: str, autor: str, paginas: int) -> None:
		self.set_titulo(titulo)
		self.set_autor(autor)
		self.set_paginas(paginas)

	def get_titulo(self) -> str:
		return self._titulo

	def set_titulo(self, titulo: str) -> None:
		if not isinstance(titulo, str) or not titulo.strip():
			raise ValueError("El título no puede ser vacío.")
		self._titulo = titulo.strip().title()

	def get_autor(self) -> str:
		return self._autor

	def set_autor(self, autor: str) -> None:
		if not isinstance(autor, str) or not autor.strip():
			raise ValueError("El autor no puede ser vacío.")
		self._autor = autor.strip().title()

	def get_paginas(self) -> int:
		return self._paginas

	def set_paginas(self, paginas: int) -> None:
		if not isinstance(paginas, int) or paginas <= 0:
			raise ValueError("Las páginas deben ser un entero > 0.")
		self._paginas = paginas

	titulo = property(get_titulo, set_titulo, doc="Título del libro.")
	autor = property(get_autor, set_autor, doc="Autor del libro.")
	paginas = property(get_paginas, set_paginas, doc="Cantidad de páginas (> 0).")

	def __repr__(self) -> str:
		return f"Libro(titulo={self._titulo!r}, autor={self._autor!r}, paginas={self._paginas})"


class Vehiculo:
	"""Vehículo motorizado.

	Atributos:
		_marca (str)
		_modelo (str)
		_anio (int) dentro de un rango razonable (1886 - año actual + 1)
		_velocidad (float) velocidad actual >= 0
	"""

	def __init__(self, marca: str, modelo: str, anio: int) -> None:
		self.set_marca(marca)
		self.set_modelo(modelo)
		self.set_anio(anio)
		self._velocidad = 0.0  # inicia en 0, solo se modifica por métodos

	# Getters/Setters básicos
	def get_marca(self) -> str:
		return self._marca

	def set_marca(self, marca: str) -> None:
		if not isinstance(marca, str) or not marca.strip():
			raise ValueError("La marca no puede ser vacía.")
		self._marca = marca.strip().title()

	def get_modelo(self) -> str:
		return self._modelo

	def set_modelo(self, modelo: str) -> None:
		if not isinstance(modelo, str) or not modelo.strip():
			raise ValueError("El modelo no puede ser vacío.")
		self._modelo = modelo.strip().title()

	def get_anio(self) -> int:
		return self._anio

	def set_anio(self, anio: int) -> None:
		from datetime import datetime
		current_year = datetime.now().year
		if not isinstance(anio, int) or not (1886 <= anio <= current_year + 1):
			raise ValueError(f"El año debe estar entre 1886 y {current_year + 1}.")
		self._anio = anio

	def get_velocidad(self) -> float:
		return self._velocidad

	# No ofrecemos setter directo de velocidad para mantener coherencia (solo métodos)

	marca = property(get_marca, set_marca, doc="Marca del vehículo.")
	modelo = property(get_modelo, set_modelo, doc="Modelo del vehículo.")
	anio = property(get_anio, set_anio, doc="Año de fabricación.")
	velocidad = property(get_velocidad, doc="Velocidad actual (solo lectura).")

	# Métodos de comportamiento
	def acelerar(self, incremento: float) -> None:
		if incremento <= 0:
			raise ValueError("El incremento debe ser > 0.")
		self._velocidad += incremento

	def frenar(self, decremento: float) -> None:
		if decremento <= 0:
			raise ValueError("El decremento debe ser > 0.")
		self._velocidad = max(0.0, self._velocidad - decremento)

	def __repr__(self) -> str:
		return ("Vehiculo(marca={m!r}, modelo={mod!r}, anio={a}, velocidad={v:.1f})"
				.format(m=self._marca, mod=self._modelo, a=self._anio, v=self._velocidad))


def _demo_objetos() -> None:
	"""Demostración de uso de las 5 clases.

	Se crean instancias, se usan setters/getters y se imprime el resultado.
	Envuelto en try/except para mostrar validaciones.
	"""
	print("=== DEMO OBJETOS ===")

	persona = Persona("ana", 20)
	print("Persona creada:", persona)
	persona.set_edad(21)
	print("Edad actualizada (getter):", persona.get_edad())
	# Uso de property
	persona.nombre = "ana maria"
	print("Nombre via property:", persona.nombre)

	cuenta = CuentaBancaria(persona, 1000)
	cuenta.depositar(250)
	try:
		cuenta.girar(2000)
	except ValueError as e:
		print("Intento de giro inválido:", e)
	cuenta.girar(500)
	print("Cuenta final:", cuenta)

	producto = Producto("abc123", "teclado mecánico", 45000)
	print("Producto:", producto)
	producto.set_precio(47000)
	print("Producto nuevo precio:", producto.precio)

	libro = Libro("el señor de los anillos", "j.r.r. tolkien", 1200)
	print("Libro:", libro)
	libro.paginas = 1210
	print("Libro páginas actualizadas:", libro.paginas)

	vehiculo = Vehiculo("toyota", "corolla", 2022)
	vehiculo.acelerar(30)
	vehiculo.acelerar(15)
	vehiculo.frenar(10)
	print("Vehículo:", vehiculo)

	# Ejemplo de validación fallida
	try:
		producto.set_precio(-5)
	except ValueError as e:
		print("Validación de precio funcionando:", e)

	print("=== FIN DEMO ===")


if __name__ == "__main__":
	_demo_objetos()
