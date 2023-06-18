import pygame
from screen import Screen
from random import choice

class Ball:

    WIDTH = 30
    HEIGHT = 30
    COLOR = (255, 255, 255)
    XSPEED = 7
    YSPEED = 7

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, Ball.WIDTH, Ball.HEIGHT)
        self.moving = True
        self.restart_mode = False
        self.restart_waiting_time = 3000
        self.restart_starting_time = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, window, left_player, right_player):
        self.check_restart_mode(window)
        self.update_speed()
        self.check_collisions(left_player, right_player)
        self.draw_ball(window)
    
    def check_restart_mode(self, window):
        if self.restart_mode:
            self.display_first_second(window)
            self.display_second_second(window)
            self.display_third_second(window)
            self.check_restart_time()

    def display_first_second(self, window):
        if pygame.time.get_ticks() - self.restart_starting_time < 1000:
            display_time = self.font.render('1', False, (255, 255, 255))
            x = (Screen.WIDTH - display_time.get_width()) / 2
            y = Screen.HEIGHT / 2 + 40
            window.blit(display_time, (x, y))
    
    def display_second_second(self, window):
        if 1000 < pygame.time.get_ticks() - self.restart_starting_time < 2000:
            display_time = self.font.render('2', False, (255, 255, 255))
            x = (Screen.WIDTH - display_time.get_width()) / 2
            y = Screen.HEIGHT / 2 + 40
            window.blit(display_time, (x, y))
    
    def display_third_second(self, window):
        if 2000 < pygame.time.get_ticks() - self.restart_starting_time < 3000:
            display_time = self.font.render('3', False, (255, 255, 255))
            x = (Screen.WIDTH - display_time.get_width()) / 2
            y = Screen.HEIGHT / 2 + 40
            window.blit(display_time, (x, y))
    
    def check_restart_time(self):
        if pygame.time.get_ticks() - self.restart_starting_time > self.restart_waiting_time:
            self.moving = True
            self.restart_mode = False

    def update_speed(self):
        if self.moving:
            self.rect.x += Ball.XSPEED
            self.rect.y += Ball.YSPEED
    
    def check_collisions(self, left_player, right_player):
        self.check_top_and_bottom_collisions(left_player, right_player)
        self.check_left_and_right_collisions(left_player, right_player)
    
    def check_top_and_bottom_collisions(self, left_player, right_player):
        if self.rect.bottom >= Screen.HEIGHT or self.rect.top <= 0:
            Ball.YSPEED *= -1
        if self.rect.colliderect(left_player.rect) or self.rect.colliderect(right_player.rect):
            Ball.XSPEED *= -1

    def check_left_and_right_collisions(self, left_player, right_player):
        if self.rect.left <= 0:
            self.update_score(right_player)
        elif self.rect.right >= Screen.WIDTH:
            self.update_score(left_player)
        if self.rect.left <= 0 or self.rect.right >= Screen.WIDTH:
            self.restart_ball_movement()

    def update_score(self, player):
        player.score += 1

    def restart_ball_movement(self):
        self.restart_mode = True
        self.moving = False
        self.restart_position()
        self.freeze_ball()
        self.randomize_speed()
    
    def restart_position(self):
        x = (Screen.WIDTH) / 2
        y = (Screen.HEIGHT) / 2
        self.rect.center = (x, y)
    
    def freeze_ball(self):
        self.restart_starting_time = pygame.time.get_ticks()

    def randomize_speed(self):
        Ball.XSPEED *= choice((1, -1))
        Ball.YSPEED *= choice((1, -1))
    
    def draw_ball(self, window):
        pygame.draw.ellipse(window, Ball.COLOR, self.rect)
