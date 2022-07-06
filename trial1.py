import pygame
import random
import math
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))

screen.fill((0,100,100))
witch=pygame.image.load("witch2.png")
x=200
y=150
x_change=0
y_change=0

mixer.music.load("bgmusic.mp3")
mixer.music.play(-1)


pygame.display.set_caption("WITCH game")
pic = pygame.image.load("witch.png")
pygame.display.set_icon(pic)

inject = pygame.image.load("meteor.png")
ix = 200
iy = 0
ix_change = 4
iy_change = 0
bullet_state = "Ready"

bgimg=pygame.image.load("xlconv.jpg")
bx=0


dragon=pygame.image.load("witch3.png")
hx=900
hy=200

dragon1=pygame.image.load("fly.png")
hx1=1500
hy1=400

alien=pygame.image.load("fear.png")
hx2=900
hy2=1500

alien2=pygame.image.load("haz.png")
hx3=1800
hy3=300


def enemie(a,b):
    screen.blit(dragon,(a,b))
    
def enemie1(a,b):
    screen.blit(dragon1,(a,b))

def enemie2(a,b):
    screen.blit(alien,(a,b))
    
def enemie3(a,b):
    screen.blit(alien2,(a,b))

def player(a,b):
    screen.blit(witch,(a,b))

def injec(a, b):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(inject, (a + 16, b + 10))


score_gained = 0
font = pygame.font.Font("freesansbold.ttf", 34)
scX = 10
scY = 10

over_font=pygame.font.Font("freesansbold.ttf",64)


def points(a, b):
    score = font.render("SCORE:" + str(score_gained), True, (240,0,255))
    screen.blit(score, (a, b))
def game_over():
    over_text = font.render("WITCH GAME made by NITHIL", True, (255, 255, 255))
    screen.blit(over_text, (200,250))




playing=True
while playing:
    esc=bx%bgimg.get_rect().width
    
    screen.blit(bgimg,(esc-bgimg.get_rect().width,0))
    if esc<800:
        screen.blit(bgimg,(esc,0))
   
    bx-=1.5
    d1=math.sqrt(((x - hx) ** 2) + ((y - hy) ** 2))
    d2=math.sqrt(((x - hx1) ** 2) + ((y - hy1) ** 2))
    d3=math.sqrt(((x - hx2) ** 2) + ((y - hy2) ** 2))
    d4=math.sqrt(((x - hx3) ** 2) + ((y - hy3) ** 2))
    distance = math.sqrt(((hx - ix) ** 2) + ((hy - iy) ** 2))
    distance1 = math.sqrt(((hx1 - ix) ** 2) + ((hy1 - iy) ** 2))
    distance2 = math.sqrt(((hx2 - ix) ** 2) + ((hy2 - iy) ** 2))
    distance3 = math.sqrt(((hx3 - ix) ** 2) + ((hy3 - iy) ** 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 2

            elif event.key == pygame.K_RIGHT:
                x_change += 2
            elif event.key == pygame.K_UP:
                y_change -= 2
            elif event.key == pygame.K_DOWN:
                y_change += 2
            elif event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    iy = y
                    ix = x
                    injec(ix, iy)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                
                x_change=0
                y_change=0
    x=x+x_change
    y=y+y_change
    if x<0:
        x=0
    if x>756:
        x=756

    #hy=hy-1
    hx=hx-2.5
    if hx<0:
        hx=random.randint(900,1000)
        hy=random.randint(100,200)
    hx1=hx1-2
    if hx1<0:
        hx1=random.randint(1200,1300)
        hy1=random.randint(300,400)
    hx2=hx2-2
    hy2=hy2-1
    if hy2<0:
        hx2=random.randint(900,1000)
        hy2=random.randint(600,700)
    hx3=hx3-2.5
    if hx3<0:
        hx3=random.randint(1300,1500)
        hy3=random.randint(300,310)
    

    
    




    if ix >800:
        ix = 200
        bullet_state = "Ready"
    if bullet_state == "Fire":
        injec(ix, iy)
        ix += ix_change

    if distance<31:
        collision_sound = mixer.Sound("strike.wav")
        collision_sound.play()
        iy=y
        bullet_state="Ready"
        hx=random.randint(900,1000)
        hy=random.randint(100,200)
        score_gained = score_gained + 1
    if distance1<31:
        collision_sound = mixer.Sound("strike.wav")
        collision_sound.play()
        iy=y
        bullet_state="Ready"
        hx1=random.randint(1200,1300)
        hy1=random.randint(300,310)
        score_gained = score_gained + 1
    if distance2<31:
        collision_sound = mixer.Sound("strike.wav")
        collision_sound.play()
        iy=y
        bullet_state="Ready"
        hx2=random.randint(400,500)
        hy2=random.randint(600,700)
        score_gained = score_gained + 1
    if distance3<31:
        collision_sound = mixer.Sound("strike.wav")
        collision_sound.play()
        iy=y
        bullet_state="Ready"
        hx3=random.randint(1300,1500)
        hy3=random.randint(300,310)
        
        score_gained = score_gained + 1
    
    if d1<27 or d2<27 or d3<27 or d4<27:
        hy=1000
        hy1=1000
        hy2=1000
        hy3=1000
        game_over()
        print("true")
        points(10,10)
        break
    
        
    
        
    
        


    player(x,y)
    enemie(hx,hy)
    enemie1(hx1,hy1)
    enemie2(hx2,hy2)
    enemie3(hx3,hy3)
    points(scX, scY)
   
    
    pygame.display.update()


