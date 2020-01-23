from RenderMain.Screen import Screen
from RenderMain.UDim2 import UDim2
from replit import clear
from RenderMain.Square import Square
from RenderMain.Texture import Texture
import time


sc = Screen()
sq = Square("Main", UDim2(20, 20), UDim2(10, 5), sc, Fill="x", Texture=Texture("Texture.txt"))
clear()
sc.Draw()