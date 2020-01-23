from RenderMain.UDim2 import UDim2

class Screen(object):
  
  """
  Defines a Screen the Code can render to,
  This must be used to define/instance
  any on-screen objects
  """
  #145, 40
  def __init__(self, Name="Main", Size=UDim2(145, 40)):
    self.Name = Name
    self.Size = Size
    self.Shapes = []
    for x in range(1, Size.x()):
      hold = []
      for y in range(1, Size.y()):
        hold.append(" ")
      self.Shapes.append(hold)
    self.Draw()

  def Draw(self):
    for y in range(1, self.Size.y()):
      for x in range(1, self.Size.x()):
        if y == 1 or y == self.Size.y()-1:
          print("-", end='')
        elif x == 1 or x == self.Size.x()-1:
          print("|",end='')
        else:
          print(self.Shapes[x-1][y-1], end='')
      print("\n", end='')
    pass

"""
=========
|       |
|       |
=========
"""