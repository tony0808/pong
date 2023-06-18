import pygame
from screen import Screen

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
    
    def draw(self, window, left_player, right_player):
        self.update_speed()
        self.check_collisions(left_player, right_player)
        pygame.draw.ellipse(window, Ball.COLOR, self.rect)
    
    def update_speed(self):
        self.rect.x += Ball.XSPEED
        self.rect.y += Ball.YSPEED
    
    def check_collisions(self, left_player, right_player):
        if self.rect.bottom >= Screen.HEIGHT or self.rect.top <= 0:
            Ball.YSPEED *= -1
        if self.rect.left <= 0 or self.rect.right >= Screen.WIDTH:
            self.restart_position()
        if self.rect.colliderect(left_player.rect) or self.rect.colliderect(right_player.rect):
            Ball.XSPEED *= -1
    
    def restart_position(self):
        x = (Screen.WIDTH - Ball.WIDTH) / 2
        y = (Screen.HEIGHT - Ball.HEIGHT) / 2
        self.rect.center = (x, y)