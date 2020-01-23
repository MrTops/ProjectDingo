class Texture:
  def __init__(self, toload):
    self.texture = [line.rstrip('\n') for line in open(toload)]