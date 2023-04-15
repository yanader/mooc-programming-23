import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

ball = pygame.image.load("ball.png")

x = 0
y = 0
velocotiy_h = 1
velocotiy_v = 1
clock = pygame.time.Clock()
width = ball.get_width()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((50,50,89))
    x+=velocotiy_h
    y+=velocotiy_v
    window.blit(ball, (x,y))

    pygame.display.flip()

    if x > 640 - width or x < 0:
        velocotiy_h *= -1
    if y > 480 - width or y < 0:
        velocotiy_v *= -1
    
    clock.tick(120)
