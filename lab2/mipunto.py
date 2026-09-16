import math


class MiPunto:
  def _init_(self, x=0.0, y=0.0):
    self._x = float(x)
    self._y = float(y)

  def get_x(self):
    return self._x

  def get_y(self):
    return self._y

 
  def distancia(self, *args):
    if len(args) == 1 and isinstance(args[0], MiPunto):
  
      otro = args[0]
      return math.sqrt(
          (self._x - otro.get_x()) * 2 + (self._y - otro.get_y()) * 2
      )
    elif len(args) == 2:

      px, py = args[0], args[1]
      return math.sqrt((self._x - px) * 2 + (self._y - py) * 2)
    else:
      raise ValueError("Parámetros no válidos para el método distancia.")



if _name_ == "_main_":

  punto1 = MiPunto()


  punto2 = MiPunto(10, 30.5)

  distancia_resultado = punto1.distancia(punto2)

  print(
      f"Coordenadas del Punto 1: ({punto1.get_x()}, {punto1.get_y()})"
  )
  print(
      f"Coordenadas del Punto 2: ({punto2.get_x()}, {punto2.get_y()})"
  )
  print(f"La distancia entre los dos puntos es: {distancia_resultado}")