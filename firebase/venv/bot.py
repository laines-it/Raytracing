import math
import random

import pygame
import sys
from PIL import Image
import numpy as np
pygame.init()
my_height = 720//2
my_wight = my_height*16/9
screen = pygame.display.set_mode((my_wight,my_height))

def drawimage(image):
    i = 0
    for line in walls:
        j = 0
        for pixel in line:
            if pixel == 1:
                color = "green"
                pygame.draw.circle(screen, color, (i, my_height - j), 1)
            j += 1
        i += 1

source_point = (my_wight//2,my_height//2)
walls_img = Image.open('walls.png').convert('L')
walls = np.array(walls_img)
walls = ~walls
walls[walls > 0] = 1
walls = np.rot90(walls,3)
pygame.draw.circle(screen,"white",source_point,2)

drawimage(walls)


for i in range(360):
    angle = math.pi * i / 180
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

