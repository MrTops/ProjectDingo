

class UDim2(object):
  def __init__(self, X, Y):
    self.X = X
    self.Y = Y
    self.Cord = {"X": X, "Y": Y}

  def x(self):
    return self.X

  def y(self):
    return self.Y

  def set_value(self, newX, newY):
    self.X = newX
    self.Y = newY
    self.Cord = {"X": newX, "Y": newY}
    return self.Cord
  
  @classmethod
  def multiply(cls, a, times):
    return UDim2(a.x() * times, a.y() * times)