import math


class AlgebraVectorial:


  def _init_(self, *args):
    if len(args) == 0:
      self.x = 0.0
      self.y = 0.0
    elif len(args) == 2:
      self.x = float(args[0])
      self.y = float(args[1])
    else:
      raise ValueError(
          "El constructor acepta 0 argumentos (0,0) o 2 argumentos (x, y)."
      )

  def producto_punto(self, b):
    return self.x * b.x + self.y * b.y

  def norma(self):
    return math.sqrt(self.x*2 + self.y*2)

  def suma(self, b):
    return AlgebraVectorial(self.x + b.x, self.y + b.y)

  def resta(self, b):
    return AlgebraVectorial(self.x - b.x, self.y - b.y)

 
  def perpendicular(self, b, opcion=3):
    if opcion == 1:
    
      return math.isclose(self.suma(b).norma(), self.resta(b).norma())
    elif opcion == 2:
      
      return math.isclose(self.resta(b).norma(), b.resta(self).norma())
    elif opcion == 3:
    
      return math.isclose(self.producto_punto(b), 0.0, abs_tol=1e-9)
    elif opcion == 4:
   
      suma_norma_cuadrada = self.suma(b).norma() ** 2
      pitagoras = self.norma() * 2 + b.norma() * 2
      return math.isclose(suma_norma_cuadrada, pitagoras, abs_tol=1e-9)
    else:
      raise ValueError("Opción de perpendicularidad no válida (1 a 4).")

  def paralela(self, b, opcion=6):
    if opcion == 5:
     
      if b.x != 0:
        r = self.x / b.x
        return math.isclose(self.y, r * b.y)
      return self.y == 0 and b.y == 0
    elif opcion == 6:
      
      cruz = self.x * b.y - self.y * b.x
      return math.isclose(cruz, 0.0, abs_tol=1e-9)
    else:
      raise ValueError("Opción de paralelismo no válida (5 o 6).")

  
  def proyeccion(self, b):
    norma_b_cuad = b.norma() ** 2
    if norma_b_cuad == 0:
      raise ValueError("No se puede proyectar sobre el vector nulo.")
    escalar = self.producto_punto(b) / norma_b_cuad
    return AlgebraVectorial(escalar * b.x, escalar * b.y)

 
  def componente(self, b):
    norma_b = b.norma()
    if norma_b == 0:
      raise ValueError("El vector b no puede tener norma cero.")
    return self.producto_punto(b) / norma_b

  def _str_(self):
    return f"({self.x}, {self.y})"



  v1 = AlgebraVectorial(3, 4)
  v2 = AlgebraVectorial(-4, 3)

  print(f"Vector 1: {v1}")
  print(f"Vector 2: {v2}")

  
  print(f"¿Son perpendiculares (a . b == 0)?: {v1.perpendicular(v2, opcion=3)}")

  
  print(
      f"¿Son paralelos (a x b == 0)?: {v1.paralela(AlgebraVectorial(6, 8), opcion=6)}"
  )

  
  proj = v1.proyeccion(v2)
  print(f"Proyección de v1 sobre v2: {proj}")

  
  comp = v1.componente(v2)
  print(f"Componente de v1 en la dirección de v2: {comp}")