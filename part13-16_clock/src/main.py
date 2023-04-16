import pygame
import time
import math

pygame.init()
display = pygame.display.set_mode((640, 480))

center_tup = (320,240)
background_rgb = (50,50,89)
foreground_rgb = (200,188,35)
clock = pygame.time.Clock()

second_hand_length = 200
minute_hand_length = 150
hour_hand_length = 90


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    

    display.fill(background_rgb)

    pygame.draw.circle(display, foreground_rgb,center_tup,200, width=3)
    pygame.draw.circle(display, foreground_rgb,center_tup,2)

    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    second_angle = seconds * 6 - 90 #multipy seconds by 6 because there are 360 degress in a circle.
    minute_angle = minutes * 6 - 90
    hour_angle = hours * 360 / 24 - 180

    second_radian = math.radians(second_angle) #convert angle to radian
    minute_radian = math.radians(minute_angle)
    hour_radian = math.radians(hour_angle)

    second_end_x = center_tup[0] + second_hand_length * math.cos(second_radian)
    second_end_y = center_tup[1] + second_hand_length * math.sin(second_radian)
    minute_end_x = center_tup[0] + minute_hand_length * math.cos(minute_radian)
    minute_end_y = center_tup[1] + minute_hand_length * math.sin(minute_radian)
    hour_end_x = center_tup[0] + hour_hand_length * math.cos(hour_radian)
    hour_end_y = center_tup[1] + hour_hand_length * math.sin(hour_radian)

    game_font = pygame.font.SysFont("Arial", 24)

    time_f_string = f'{hours:2}:{minutes:2}:{seconds:2}'
    time_text = game_font.render(time_f_string, True, foreground_rgb)
    
    display.blit(time_text, (100, 50))


    pygame.draw.line(display,foreground_rgb,center_tup,(second_end_x, second_end_y),2)
    pygame.draw.line(display,foreground_rgb,center_tup,(minute_end_x, minute_end_y),4)
    pygame.draw.line(display,foreground_rgb,center_tup,(hour_end_x, hour_end_y),4)
    pygame.display.flip()
    clock.tick(60)