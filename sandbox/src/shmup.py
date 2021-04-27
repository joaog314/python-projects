# Pygame template - skeleton for a new pygmae project
import pygame as pg 
import random

WIDTH = 900
HEIGHT = 500
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
pg.display.set_caption("Shmup")
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    
    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH 

class Mob(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 10
        self.rect.x = WIDTH - self.rect.width #random.randrange(-100, -40)
        self.speedx = random.randrange(-8,-1)
 
    def update(self):
        self.rect.x += self.speedx*0.7
        if self.rect.right > WIDTH:
            # self.rect.x = random.randrange(HEIGHT - self.rect.height)
            self.speedx = self.speedx*-1
        if self.rect.left < 0:
            # self.rect.x = random.randrange(HEIGHT - self.rect.height)
            self.speedx = self.speedx*-1


# sprites
all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

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