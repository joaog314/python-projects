from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(800,800)
janela.set_title("Pong")

teclado = Window.get_keyboard()


fundo = GameImage("nebula.jpg")
bolinha = Sprite("bola.png",1)
padE = Sprite("pad.png",1)
padD = Sprite("pad.png",1)

velx = 100
vely = 100
velPad = 250


bolinha.x = janela.width/2 - bolinha.width/2
bolinha.y = janela.height/2 - bolinha.height/2

padE.x = 5
padD.x = janela.width - padD.width - 5
padE.y = janela.height/2 - padD.height/2
padD.y = janela.height/2 - padD.height/2

#pontos

pontos1 = 0
pontos2 = 0

while(True):

    if(teclado.key_pressed("UP")):
        if (padE.y > 0):
            padE.y = padE.y - velPad * janela.delta_time()
    if(teclado.key_pressed("DOWN")):
        if (padE.y + padE.height < janela.height):
            padE.y = padE.y + velPad * janela.delta_time()

    if(teclado.key_pressed("W")):
        if (padD.y > 0):
            padD.y = padD.y - velPad * janela.delta_time()
    if(teclado.key_pressed("S")):
        if (padD.y + padD.height < janela.height):
            padD.y = padD.y + velPad * janela.delta_time()
    

    #updates
    bolinha.x = bolinha.x + velx * janela.delta_time()
    bolinha.y = bolinha.y + vely * janela.delta_time()

    if ((bolinha.x + bolinha.width) > janela.width):
        pontos1 += 1
        bolinha.x = janela.width/2 - bolinha.width/2
        bolinha.y = janela.height/2 - bolinha.height/2
    if (bolinha.x < 0): 
        pontos2 += 1
        bolinha.x = janela.width/2 - bolinha.width/2
        bolinha.y = janela.height/2 - bolinha.height/2
    if ((bolinha.y + bolinha.height) > janela.height):
        vely = vely *-1
    if (bolinha.y < 0):
        vely = vely *-1
     #colisao da bolinha 
    if padE.collided(bolinha):
        velx = velx *-1
    if padD.collided(bolinha):
        velx = velx *-1
       

    #desenho
    fundo.draw()
    bolinha.draw()
    padE.draw()
    padD.draw()
    janela.draw_text(str(pontos1), 10, 10, size=40, color=(255,255,255), font_name='Arial', bold=True, italic=False)
    janela.draw_text(str(pontos2), janela.width - 40, 10, size=40, color=(255,255,255), font_name='Arial', bold=True, italic=False)
    janela.update()


