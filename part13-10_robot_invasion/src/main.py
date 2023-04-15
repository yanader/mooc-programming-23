# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")
coordinates = []



height = robot.get_height()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    window.fill((50,50,89))
    if random.randint(1,100) == 100:
        x = random.randint(0,640)
        coordinates.append([x,0])

    for coordinate in coordinates:
        window.blit(robot,(coordinate[0],coordinate[1]))
        if coordinate[1] < 480 - height:
            coordinate[1] +=1
        else:
            coordinate[1] = 480 - height
            if coordinate[0] < 320:
               coordinate[0] -= 1
            else:
               coordinate[0] += 1

    pygame.display.flip()

    clock.tick(120)