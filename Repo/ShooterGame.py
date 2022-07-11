import pygame
from random import *

pygame.init()
clock = pygame.time.Clock()
FPS = 60

win_width = 750
win_height =700
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Space Shooter")
background = pygame.transform.scale(pygame.image.load("spaceBG.jpg"),(win_width, win_height))
window.blit(background,(0, 0))

pygame.font.init()

pygame.mixer.init()
pygame.mixer.music.load("SpaceMusic.mp3")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play()

#The SpaceHero-Sprite Class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y):
        super().__init__()
        self.image=player_image
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_image=pygame.transform.scale(pygame.image.load("spaceship2.png"), (100, 90))
player_x=280
player_y=400
player_speed=10
GameS=GameSprite(player_image,player_speed,player_x,player_y)

player_image3=pygame.transform.scale(pygame.image.load("spaceship2.png"), (30, 30))
player_image4=pygame.transform.scale(pygame.image.load("spaceship2.png"), (30, 30))
player_image5=pygame.transform.scale(pygame.image.load("spaceship2.png"), (30, 30))

#The Invaders Class
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self,player_image2,player_speed2,player_x2,player_y2):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load(player_image2), (80, 90))
        self.speed=player_speed2
        self.rect=self.image.get_rect()
        self.rect.x= player_x2
        self.rect.y= player_y2
    def reset2(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(EnemySprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            player_image3.fill((255,255,255,0))
        window.blit(self.image, (self.rect.x, self.rect.y))

player_image2="invaderG.png"
player_x2=300
player_y2=20
player_speed2=randint(4,10)

EnemyS=Enemy(player_image2,player_speed2,player_x2,player_y2)

invaders = pygame.sprite.Group()

invader2=Enemy(player_image2,randint(4,8),player_x2,player_y2)
invader3=Enemy(player_image2,randint(4,8),player_x2,player_y2)
invader4=Enemy(player_image2,randint(4,8),player_x2,player_y2)
invader5=Enemy(player_image2,randint(4,8),player_x2,player_y2)
invader6=Enemy(player_image2,randint(4,8),player_x2,player_y2)

invaders.add(invader2,invader3,invader4,invader5,invader6)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        window.blit(self.image, (self.rect.x, self.rect.y))
            

bullet_image=pygame.transform.scale(pygame.image.load("lazerB.png"), (60, 50))
bullet_x=280
bullet_y=400
bullet_speed=-20

player_image3=pygame.transform.scale(pygame.image.load("spaceship2.png"), (30, 30))
player_image4=pygame.transform.scale(pygame.image.load("spaceship2.png"), (30, 30))
player_image5=pygame.transform.scale(pygame.image.load("spaceship2.png"), (30, 30))

bulletGr=pygame.sprite.Group()

c=0

Hits=0

game =True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background,(0, 0))
    window.blit(GameS.image,(player_x, player_y))
    window.blit(player_image3,(10,20))
    window.blit(player_image4,(50,20))
    window.blit(player_image5,(90,20))

    invaders.update()

    c=c+1


    #Keys for moving spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 5:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x <win_width - 80:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 5:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < win_height - 80:
        player_y += player_speed

    if c%12==0:
        if keys[pygame.K_SPACE]:
            b=Bullet(bullet_image,player_speed,player_x,player_y)
            bulletGr.add(b)

    
    for b in bulletGr:
        if pygame.sprite.spritecollide(b,invaders,True):
            b.kill()
            Hits=Hits+1
            e=Enemy(player_image2,randint(4,8),randint(20,500),player_y2)
            invaders.add(e)
    font1 = pygame.font.Font(None, 30)
    text_lose = font1.render("Hits: " + str(Hits), 1, (200, 50, 255))
    window.blit(text_lose,(20,60))

    bulletGr.update()
    
    clock.tick(FPS)
    pygame.display.update()