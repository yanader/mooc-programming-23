import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

height = robot.get_height()
width = robot.get_width()
print(height)
print(width)
x1, x2 = 50, 300
y1, y2 = 50, 300

to_left1, to_left2 = False, False
to_right1, to_right2 = False, False
to_top1, to_top2 = False, False
to_bottom1, to_bottom2 = False, False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_left1 = True
            if event.key == pygame.K_d:
                to_right1 = True
            if event.key == pygame.K_w:
                to_top1 = True
            if event.key == pygame.K_s:
                to_bottom1 = True
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left2 = True
            if event.key == pygame.K_RIGHT:
                to_right2 = True
            if event.key == pygame.K_UP:
                to_top2 = True
            if event.key == pygame.K_DOWN:
                to_bottom2 = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                to_left1 = False
            if event.key == pygame.K_d:
                to_right1 = False
            if event.key == pygame.K_w:
                to_top1 = False
            if event.key == pygame.K_s:
                to_bottom1 = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left2 = False
            if event.key == pygame.K_RIGHT:
                to_right2 = False
            if event.key == pygame.K_UP:
                to_top2 = False
            if event.key == pygame.K_DOWN:
                to_bottom2 = False


    if to_right1:
        if x1 < 640 - width:
            x1+=2
    if to_left1:
        if x1 > 0:
            x1-=2
    if to_top1:
        if y1 > 0:
            y1-=2
    if to_bottom1:
        if 1 < 480 - height:
            y1+=2

    if to_right2:
        if x2 < 640 - width:
            x2+=2
    if to_left2:
        if x2 > 0:
            x2-=2
    if to_top2:
        if y2 > 0:
            y2-=2
    if to_bottom2:
        if 1 < 480 - height:
            y2+=2
    
    window.fill((50,50,89))
    window.blit(robot,(x1,y1))
    window.blit(robot,(x2,y2))
    pygame.display.flip()
    clock.tick(120)

        