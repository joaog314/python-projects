# Pygame template - skeleton for a new pygmae project
import pygame as pg 
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# iniciando o pygame e criando a janela
pg.init()
# to init sound
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

# sprites
all_sprites = pg.sprite.Group()

# Game loop

running = True
while running:
    # manter o fps constante 
    clock.tick(FPS)
    # processo de entrada (eventos)
    for event in pg.event.get():
        # checando açao de fechar a janela
        if event.type == pg.QUIT:
            running = False
    
    # update
    all_sprites.update()

    
    # draw / renderizar
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *depois* de desenhar tudo, muda o display
    pg.display.flip()

pg.quit()