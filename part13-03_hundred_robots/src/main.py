import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
window.fill((50,50,89))
x, y = 25, 100

for i in range(10):
    for j in range(10):
        window.blit(robot,(x,y))
        x += width
    y+= height/4
    x = (25 + width/4) + (i * width/4)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
