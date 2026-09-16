import math


class VectorTridimensional:

  def _init_(self, a1=0.0, a2=0.0, a3=0.0):
    self.a1 = float(a1)
    self.a2 = float(a2)
    self.a3 = float(a3)


  def _add_(self, otro):
    if isinstance(otro, VectorTridimensional):
      return VectorTridimensional(
          self.a1 + otro.a1, self.a2 + otro.a2, self.a3 + otro.a3
      )
    raise TypeError("El operando debe ser un VectorTridimensional.")

  def _mul_(self, escalar):
    if isinstance(escalar, (int, float)):
      return VectorTridimensional(
          escalar * self.a1, escalar * self.a2, escalar * self.a3
      )
    raise TypeError("El multiplicador debe ser un número (int o float).")

  def _rmul_(self, escalar):
    return self._mul_(escalar)


  def _abs_(self):
    return math.sqrt(self.a1*2 + self.a22 + self.a3*2)

  def normal(self):
    longitud = abs(self)
    if longitud == 0:
      raise ValueError(
          "No se puede calcular la normal del vector nulo (longitud 0)."
      )
    return VectorTridimensional(
        self.a1 / longitud, self.a2 / longitud, self.a3 / longitud
    )

  def producto_escalar(self, otro):
    if isinstance(otro, VectorTridimensional):
      return self.a1 * otro.a1 + self.a2 * otro.a2 + self.a3 * otro.a3
    raise TypeError("El operando debe ser un VectorTridimensional.")

  def producto_vectorial(self, otro):
    if isinstance(otro, VectorTridimensional):
      v1 = self.a2 * otro.a3 - self.a3 * otro.a2
      v2 = self.a3 * otro.a1 - self.a1 * otro.a3
      v3 = self.a1 * otro.a2 - self.a2 * otro.a1
      return VectorTridimensional(v1, v2, v3)
    raise TypeError("El operando debe ser un VectorTridimensional.")

  def _str_(self):
    return f"({self.a1}, {self.a2}, {self.a3})"


if _name_ == "_main_":
  v1 = VectorTridimensional(1, 2, 3)
  v2 = VectorTridimensional(4, 5, 6)

  print(f"Vector a: {v1}")
  print(f"Vector b: {v2}\n--- Resultados ---")


  print(f"a) Suma (a + b) = {v1 + v2}")

  escalar = 2
  print(f"b) Multiplicación por escalar ({escalar} * a) = {escalar * v1}")


  print(f"c) Longitud de a (|a|) = {abs(v1):.4f}")

  print(f"d) Normal de a (vector unitario) = {v1.normal()}")

  print(f"e) Producto escalar (a . b) = {v1.producto_escalar(v2)}")

  print(f"f) Producto vectorial (a x b) = {v1.producto_vectorial(v2)}")