import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = random.randint(0,640-width)
y = random.randint(0,480-height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_click = event.dict['pos'][0]
            y_click = event.dict['pos'][1]
            if x_click > x and x_click < x + width and y_click > y and y_click < y + height:
                x = random.randint(0,640-width)
                y = random.randint(0,480-height)
                
    window.fill((50,50,89))
    window.blit(robot,(x,y))

    pygame.display.flip()
    clock.tick(60)