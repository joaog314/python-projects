from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(600,600)
background = GameImage("fundo.jpg")

while (True):
    background.draw()
    janela.update()