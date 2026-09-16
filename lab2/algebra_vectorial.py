class AlgebraVectorial:

  def _init_(self, x=0, y=0):
    self.x = x
    self.y = y

  def _str_(self):
    return f"Vector({self.x}, {self.y})"


if _name_ == "_main_":
  v1 = AlgebraVectorial(3, 4)
  print(v1)
