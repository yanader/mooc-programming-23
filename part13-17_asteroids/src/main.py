import pygame
import random

pygame.init()
window = pygame.display.set_mode((640,480))

rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")
coordinates = []

rock_height = rock.get_height()

robot_x = 320
robot_height = robot.get_height()
robot_width = robot.get_width()
robot_y = 480 - robot_height
move_left = False
move_right = False
score = 0
game_over = False
clock = pygame.time.Clock()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
    
    if move_right:
        robot_x+=2
    if move_left:
        robot_x-=2

    window.fill((50,50,89))
    window.blit(robot,(robot_x, robot_y))

    if random.randint(1,200) == 200:
        x= random.randint(0,640)
        coordinates.append([x,0])
    
    for coordinate in coordinates:
        if coordinate[1] + rock_height > 480 - robot_height:
            if coordinate[0] > robot_x and coordinate[0] < robot_x + robot_width:
                score+=1
                coordinates.remove(coordinate)
        
    for coordinate in coordinates:
        window.blit(rock,(coordinate[0],coordinate[1]))
        if coordinate[1] < 480 - rock_height:
            coordinate[1]+=1
        if coordinate[1] >= 480 - rock_height:
            game_over = True
            break

    score_string = f'Points: {score}'
    game_font = pygame.font.SysFont("Arial", 24)
    score_display = game_font.render(score_string,True,(255,0,0))
    window.blit(score_display,(550,10))

    if game_over:
        end_font = pygame.font.SysFont("Arial", 48)
        end_string = f'You ate {score} rocks!'
        end_display = end_font.render(end_string,True,(255,0,0))
        window.blit(end_display,(220,240))

    pygame.display.flip()
    clock.tick(120)

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((50,50,89))

    end_font = pygame.font.SysFont("Arial", 48)
    end_string = f'You ate {score} rocks!'
    end_display = end_font.render(end_string,True,(255,0,0))
    window.blit(end_display,(220,240))

    pygame.display.flip()