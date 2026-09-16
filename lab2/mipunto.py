import math


class MiPunto:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

  def distancia(self, otro_punto):
    return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

  def __str__(self):
    return f"{self.x}, {self.y}"


if __name__ == "__main__":
  punto1 = MiPunto(2, 3)
  punto2 = MiPunto(7, 11)

  print(f"Punto 1: {punto1}")
  print(f"Punto 2: {punto2}")
  print("La distancia es:", punto1.distancia(punto2))
