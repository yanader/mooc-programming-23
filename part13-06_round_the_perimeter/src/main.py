import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocityX = 1
velocityY = 0

width = robot.get_width()
height = robot.get_height()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((50,50,89))
    window.blit(robot,(x,y))
    pygame.display.flip()

    x+= velocityX
    y+= velocityY

    if velocityX > 0 and x+width >= 640:
        velocityX = 0
        velocityY = 1
    if velocityY > 0 and y+height >= 480:
        velocityX = -1
        velocityY = 0
    if velocityX < 0 and x <= 0:
        velocityX = 0
        velocityY = -1
    if velocityY < 0 and y <= 0:
        velocityX = 1
        velocityY = 0
    clock.tick(60)