class VectorTridimensional:

  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    return f"Vector3D({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
  v1 = VectorTridimensional(1, 2, 3)
  print(v1)
