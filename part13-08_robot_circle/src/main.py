import pygame
import math

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

x1 = 0
y1 = 50
x2 = 0
y2 = 150
radius = 150
number = 10
width = robot.get_width()
height = robot.get_height()


angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        

    window.fill((50, 50, 89))
    for i in range(10):
        x = 640/2+math.cos(angle+2*math.pi*i/number)*radius-width/2
        y = 480/2+math.sin(angle+2*math.pi*i/number)*radius-height/2
        window.blit(robot, (x, y))
        

    
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)