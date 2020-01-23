class Square:
  def __init__(self, Name, Size, Position, Screen, Fill="#", Texture="none"):
    if Texture != "none":
      for x in range(1, Size.x()):
        for y in range(1, Size.y()):
          if not y%len(Texture.texture) == 0:
            if not x%len(Texture.texture[y%len(Texture.texture)]) == 0:
              Screen.Shapes[x+Position.x()][y+Position.y()] = Texture.texture[y%len(Texture.texture)][x%len(Texture.texture[y%len(Texture.texture)])]
            else:
              Screen.Shapes[x+Position.x()][y+Position.y()] = Texture.texture[y%len(Texture.texture)][-1]
          else:
            if not x%len(Texture.texture[-1]) == 0:
              Screen.Shapes[x+Position.x()][y+Position.y()] = Texture.texture[-1][x%len(Texture.texture[-1])]
            else:
              Screen.Shapes[x+Position.x()][y+Position.y()] = Texture.texture[-1][-1]
    else:
      for x in range(1, Size.x()):
        for y in range(1, Size.y()):
          Screen.Shapes[x+Position.x()][y+Position.y()] = Fill