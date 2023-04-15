# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    window.fill((50,50,89))
    window.blit(robot,(x,y))
    pygame.display.flip()

    y+=velocity
    if velocity > 0 and y+robot.get_height()>= 480:
        velocity*=-1
    if velocity < 0 and y <= 0:
        velocity*=-1
    clock.tick(60)