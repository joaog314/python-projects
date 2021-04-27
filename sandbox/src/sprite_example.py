# Pygame template - skeleton for a new pygmae project
import pygame as pg 
import random
import os

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# set up assets folders
game_folder = os.path.dirname(__file__)
# output /Users/joaogngs/Documents/GitHub/uff-projects/sandbox/src
img_folder = os.path.join(game_folder, "img")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "idle-Sheet.png"))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = - 5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.x > WIDTH:
            self.rect.right = 0
# iniciando o pygame e criando a janela
pg.init()
# to init sound
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Ninja test")
clock = pg.time.Clock()

# sprites
all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *depois* de desenhar tudo, muda o display
    pg.display.flip()

pg.quit()