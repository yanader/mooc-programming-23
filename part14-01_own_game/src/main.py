import pygame
import random
# control the robot
# colect the coins
# avoid the monster that is coming for you
# maybe pay some coints to build a door to stun the monster

class CapitalistMonster:
    def __init__(self):
        pygame.init()

        self.load_images()
        
        self.start_game()
        self.main_loop()
    
    def load_images(self):
        self.images = []
        for name in ['coin','door','monster','robot']:
            self.images.append(pygame.image.load(name + ".png"))
    
    def main_loop(self):
        while not self.game_over:
            self.check_events()
            self.move_monster()
            self.move_robot()
            self.draw_window()
            if self.coin_collect():
                self.score += 1
                self.coin_x = random.randint(0, self.window_width - self.coin_width)
                self.coin_y = random.randint(0, self.window_height - self.coin_height)
            if self.player_died():
                self.end_game()
        
            while self.game_over:
                self.check_for_reset()
                self.draw_game_over_window()
        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_up = True
                if event.key == pygame.K_DOWN:
                    self.move_down = True
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.move_up = False
                if event.key == pygame.K_DOWN:
                    self.move_down = False
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                if event.key == pygame.K_RIGHT:
                    self.move_right = False

    def check_for_reset(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.start_game()
                if event.key != pygame.K_F1:
                    pass

    def player_died(self):
        if self.monster_x > self.robot_x - self.monster_width and \
            self.monster_x < self.robot_x + self.robot_width and \
                self.monster_y > self.robot_y - self.monster_height and \
                    self.monster_y < self.robot_y + self.robot_height:
            return True
        else:
            return False
    
    def end_game(self):
        self.game_over = True

    def start_game(self):
        self.game_over = False
        self.score = 0

        self.window_height = 720
        self.window_width = 1280
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.game_font = pygame.font.SysFont("score_text", 28)

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.robot_x = 50
        self.robot_y = 600
        self.robot_width = self.images[3].get_width()
        self.robot_height = self.images[3].get_height()
        
        self.monster_x = 1230
        self.monster_y = 100
        self.monster_width = self.images[2].get_width()
        self.monster_height = self.images[2].get_height()

        self.coin_width = self.images[0].get_width()
        self.coin_height = self.images[0].get_height()
        self.coin_x = random.randint(0, self.window_width - self.coin_width)
        self.coin_y = random.randint(0, self.window_height - self.coin_height)

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("!! CAPITALIST MONSTER !!")
        self.main_loop()


    def coin_collect(self):
        if self.coin_x > self.robot_x - self.coin_width and \
            self.coin_x < self.robot_x + self.robot_width and \
                self.coin_y > self.robot_y - self.coin_height and \
                    self.coin_y < self.robot_y + self.robot_height:
            return True


    def move_robot(self):
        robot_speed = 2
        if self.move_up and self.robot_y > 0:
            self.robot_y-=robot_speed
        if self.move_down and self.robot_y < self.window_height - self.robot_height:
            self.robot_y+=robot_speed
        if self.move_left and self.robot_x > 0:
            self.robot_x-=robot_speed
        if self.move_right and self.robot_x < self.window_width - self.robot_width:
            self.robot_x+=robot_speed

    def move_monster(self):
        monster_speed = 1
        if self.monster_y < self.robot_y:
            self.monster_y+=monster_speed
        elif self.monster_y > self.robot_y:
            self.monster_y-=monster_speed
        if self.monster_x < self.robot_x:
            self.monster_x+=monster_speed
        elif self.monster_x > self.robot_x:
            self.monster_x-=monster_speed
    
    def draw_window(self):
        self.window.fill((50,50,89))
        score_text = self.game_font.render("$$$" + str(self.score), True, (200,200,200))

        self.window.blit(self.images[0], (self.coin_x, self.coin_y))
        self.window.blit(self.images[2], (self.monster_x, self.monster_y))
        self.window.blit(self.images[3], (self.robot_x, self.robot_y))
        self.window.blit(score_text, (20, 20))
        
        pygame.display.flip()
        self.clock.tick(120)

    def draw_game_over_window(self):
        while self.game_over:
            self.window.fill((50,50,89))
            self.game_font = pygame.font.SysFont("Verdana", 66)
            gameover = "!! GAME OVER !!"
            plural = ""
            newgame = "PRESS F1 TO PLAY AGAIN"
            if self.score != 1:
                plural = "s"
            finalscore = "You collected " + str(self.score) + " coin" + plural + "!!"
            end_text = self.game_font.render(f"{gameover:^30}", True, (200,200,200))
            score_text = self.game_font.render(f"{finalscore:^30}", True, (200,200,200))
            newgame_text = self.game_font.render(f"{newgame:^30}", True, (200,200,200))
            self.window.blit(end_text, (200, 200))
            self.window.blit(score_text, (200, 270))
            self.window.blit(newgame_text, (120, 350))
            self.check_for_reset()
            pygame.display.flip()


if __name__ == "__main__":
    CapitalistMonster()
