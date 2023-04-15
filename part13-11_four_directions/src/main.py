import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

x = 320
y = 240

to_left = False
to_right = False
to_top = False
to_bottom = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_top = True
            if event.key == pygame.K_DOWN:
                to_bottom = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_top = False
            if event.key == pygame.K_DOWN:
                to_bottom = False

    if to_right:
        x+=2
    if to_left:
        x-=2
    if to_top:
        y-=2
    if to_bottom:
        y+=2
    
    window.fill((50,50,89))
    window.blit(robot,(x,y))
    pygame.display.flip()
    clock.tick(120)

        