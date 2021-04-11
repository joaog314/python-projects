from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random 

janela = Window(800,800)
janela.set_title("Pong")

teclado = Window.get_keyboard()


fundo = GameImage("space-invaders/images/nebula.jpg")
spaceship = Sprite("space-invaders/images/spaceship.png",1)
bullet = Sprite("space-invaders/images/bullet.png",1)

# bullets list
shot = [bullet]*5

velx = 100
vely = 50 #random.randint(-200, 200)
velPad = 150

spaceship.x = janela.width/2 - spaceship.width/2
spaceship.y = janela.height - spaceship.height

# bullet.x = janela.width/2 - bullet.width/2
# bullet.y = janela.height/2 - bullet.height/2

# spaceship.x = janela.width/2 - spaceship.width/2
# spaceship.y = janela.height - spaceship.height



#pontos

# pontos1 = 0
# pontos2 = 0

#frame rate 

t_delta = 1
# frame_rt = 0
# frames = 0

# collided count

col_count = 0

while(True):

    t_delta += janela.delta_time()

    if(teclado.key_pressed("LEFT")):
        if (spaceship.x > 0):
            spaceship.x = spaceship.x - velPad * janela.delta_time()
    if(teclado.key_pressed("RIGHT")):
        if (spaceship.x + spaceship.width < janela.height):
            spaceship.x = spaceship.x + velPad * janela.delta_time()

    for i in shot[n]
        shot[n].x = spaceship.x + spaceship.width/2 - shot.width/2
        shot[n].y = spaceship.y
        shot[n].y = shot[n].y - vely * janela.delta_time()
        print(type)
        return shot[n]

    
    #desenho
    fundo.draw()
    #shot.draw()
    bullet.draw()
    spaceship.draw()
    # janela.draw_text(str(pontos1), 10, 10, size=40, color=(255,255,255), font_name='Arial', bold=True, italic=False)
    # janela.draw_text(str(pontos2), janela.width - 40, 10, size=40, color=(255,255,255), font_name='Arial', bold=True, italic=False)
    # janela.draw_text("FPS:"+str(int(frame_rt)), janela.width - 100, janela.height - 40, size=20, color=(255,255,255), font_name='Arial', bold=False, italic=False)
        


