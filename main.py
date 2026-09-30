import pygame
import random
import math

screen_width = 1280
screen_height = 740
player_start_x = 600
player_start_y = 650
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 1.5
enemy_speed_y = 15
bullet_speed_y = 10
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('space invaders.jpg')
background = pygame.transform.scale(
    background,(screen_width,screen_height)
)
pygame.display.set_caption('space invaders')

playerimg = pygame.image.load('UFO1.png')
playerimg = pygame.transform.scale(playerimg,(60,60))
playerx = player_start_x
playery = player_start_y
playerxchange = 0

enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy = pygame.image.load('ALIEN.png')
    enemy = pygame.transform.scale(enemy,(50,50))
    enemyimg.append(enemy)
    enemyx.append(random.randint(0,screen_width - 50))
    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyxchange.append(enemy_speed_x)
    enemyychange.append(enemy_speed_y)

bulletimg = pygame.image.load('bullets.png')
bulletimg = pygame.transform.scale(bulletimg,(30,30))
bulletx = 0
bullety = player_start_y
bullet_y_change = bullet_speed_y
bullet_state = 'ready'
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render('score'+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    game_over = font.render('game over',True,(255,255,255))
    screen.blit(game_over,(600,300))

def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg,(x + 16,y + 10))

def is_collision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt(
        (enemyx - bulletx)** 2 + 
        (enemyy - bullety)** 2 
    )
    return distance < collision_distance

running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -5
            if event.key == pygame.K_RIGHT:
                playerxchange = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletx = playerx
                    fire_bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                playerxchange = 0
    playerx += playerxchange
    playerx = max(0,min(playerx,screen_width - 60))

    for i in range(num_of_enemies):
        if enemyy[i]> 600:
            for j in range(num_of_enemies):
                enemyy[j]= 2000
            game_over_text()
            break
        enemyx[i]+= enemyxchange[i]
        if enemyx[i]<= 0 or enemyx[i]>= screen_width - 50:
            enemyxchange[i]*= -1
            enemyy[i]+= enemyychange[i]

        if  is_collision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety = player_start_y
            bullet_state = 'ready'
            score_value += 1
            enemyx[i]= random.randint(0,screen_width - 50)
            enemyy[i]= random.randint(enemy_start_y_min,enemy_start_y_max)
        enemy(enemyx[i],enemyy[i],i)

    if bullety <= 0:
            bullety = player_start_y
            bullet_state = 'ready'
    elif bullet_state == 'fire':
        fire_bullet(bulletx,bullety)
        bullety -= bullet_y_change

    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()

pygame.quit()