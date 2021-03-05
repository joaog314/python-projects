from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random 

janela = Window(800,800)
janela.set_title("Pong")

teclado = Window.get_keyboard()


fundo = GameImage("nebula.jpg")
bolinha = Sprite("bola.png",1)
bolinha2 = Sprite("bola.png",1)
padE = Sprite("pad.png",1)
padD = Sprite("pad.png",1)

velx = 100
vely = 200 #random.randint(-200, 200)
velPad = 150


bolinha.x = janela.width/2 - bolinha.width/2
bolinha.y = janela.height/2 - bolinha.height/2

padE.x = 5
padD.x = janela.width - padD.width - 5
padE.y = janela.height/2 - padD.height/2
padD.y = janela.height/2 - padD.height/2

#pontos

pontos1 = 0
pontos2 = 0

#frame rate 

t_delta = 0
frame_rt = 0
frames = 0

# collided count

col_count = 0

while(True):

    if(teclado.key_pressed("UP")):
        if (padE.y > 0):
            padE.y = padE.y - velPad * janela.delta_time()
    if(teclado.key_pressed("DOWN")):
        if (padE.y + padE.height < janela.height):
            padE.y = padE.y + velPad * janela.delta_time()
    
    #ia
    if vely < 0:
        if (padD.y > 0):
            padD.y = padD.y - velPad * janela.delta_time()
    if vely > 0:
        if (padD.y + padD.height < janela.height):
            padD.y = padD.y + velPad * janela.delta_time()
    
    #updates
    bolinha.x = bolinha.x + velx * janela.delta_time()
    bolinha.y = bolinha.y + vely * janela.delta_time()

    if ((bolinha.x + bolinha.width) > janela.width):
        pontos1 += 1
        bolinha.x = janela.width/2 - bolinha.width/2
        bolinha.y = janela.height/2 - bolinha.height/2
        velx = 100
        vely = random.randint(-100, 100)
        
    if (bolinha.x < 0): 
        pontos2 += 1
        bolinha.x = janela.width/2 - bolinha.width/2
        bolinha.y = janela.height/2 - bolinha.height/2
        velx = - 100
        vely = random.randint(-100, 100)

    if ((bolinha.y + bolinha.height) > janela.height):
        vely = vely *-1
        
    if (bolinha.y < 0):
        vely = vely *-1



     #colisao da bolinha 
    if padE.collided(bolinha):
        bolinha.x += 10     
        velx = velx *-1
        col_count +=1

    if padD.collided(bolinha):
        bolinha.x -= 10
        velx = velx *-1
        col_count +=1

    # calculo de frames
    t_delta += janela.delta_time()
    frames += 1
    if t_delta >= 1:
        frame_rt = frames/t_delta
        t_delta = 0
        frames = 0
        
    if col_count == 3:
        bolinha2.draw()
        
    #desenho
    fundo.draw()
    bolinha.draw()
    padE.draw()
    padD.draw()
    janela.draw_text(str(pontos1), 10, 10, size=40, color=(255,255,255), font_name='Arial', bold=True, italic=False)
    janela.draw_text(str(pontos2), janela.width - 40, 10, size=40, color=(255,255,255), font_name='Arial', bold=True, italic=False)
    janela.draw_text("FPS:"+str(int(frame_rt)), janela.width - 100, janela.height - 40, size=20, color=(255,255,255), font_name='Arial', bold=False, italic=False)
    janela.update()


