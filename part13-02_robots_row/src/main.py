# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
window.fill((50,50,89))
x = 50
y = 50
for i in range (10):
    window.blit(robot,(x,y))
    x += width
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()