import pygame
import random
import math

screen_width = 1280
screen_height = 740
player_start_x = 600
player_start_y = 700
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
score = 0
font = pygame.font.Font('freesansbold.ttf',64)