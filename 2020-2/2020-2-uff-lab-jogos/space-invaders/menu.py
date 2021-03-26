from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *               


janela = Window(800,800)
janela.set_title("Space Invaders")

teclado = Window.get_keyboard()
mouse = Window.get_mouse()


fundo = GameImage("space-invaders/images/nebula.jpg")
button_play = GameImage("space-invaders/images/jogar.jpg")
button_dif = GameImage("space-invaders/images/dificu.jpg")
button_exit = GameImage("space-invaders/images/sair.jpg")
button_ranking = GameImage("space-invaders/images/ranking.jpg")

button_play.x = janela.width/2 - button_play.width/2
button_play.y = janela.height/4.5 - button_play.height

button_dif.x = janela.width/2 - button_play.width/2
button_dif.y = janela.height/2.2 - button_play.height

button_ranking.x = janela.width/2 - button_play.width/2
button_ranking.y = janela.height/1.5 - button_play.height

button_exit.x = janela.width/2 - button_exit.width/2
button_exit.y = janela.height/1.1 - button_exit.height

def playgame():

    while(True):

        if(teclado.key_pressed("ESC")):
            
            break

        else:

            #desenho
            fundo.draw()
            janela.update()


while(True):

    # if(mouse.is_button_pressed(3)):
    #    vetor = mouse.get_position()
    #     if vetor >= ()
    
        #desenho
        fundo.draw()
        button_play.draw()
        button_exit.draw()
        button_ranking.draw()
        button_dif.draw()
        janela.update()


