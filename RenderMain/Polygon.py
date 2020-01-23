from RenderMain.UDim2 import UDim2

class Polygon:

  def __init__(self, screen, scale, fill, *points):
    self.scale = scale
    self.screen = screen
    self.fill = fill
    self.x_points = []
    self.y_points = []
    #Sets the points to be scaled
    i = 0
    hold = []
    for point in points:
      hold.append(UDim2(point.X * self.scale, point.Y * self.scale))
      self.x_points.append(point.X * self.scale)
      self.y_points.append(point.Y * self.scale)
      i += 1
    self.points = hold

    mark_line = False
    line_value = 0
    add = 0
    index = 0
    for x in range(1, self.screen.x()):      
      for y in range(1, self.screen.y()):
        pass
        #YEA NO
        