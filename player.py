import pygame
from screen import Screen

class Player:

    WIDTH = 10
    HEIGHT = 140
    COLOR = (255, 255, 255)
    SPEED = 7

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.rect = pygame.Rect(x, y, Player.WIDTH, Player.HEIGHT)

    def draw(self, window):
        self.update_speed()
        self.check_collisions()
        pygame.draw.rect(window, Player.COLOR, self.rect)

    def update_speed(self):
        self.rect.y += self.speed
    
    def check_collisions(self):
        if self.rect.top <= 5:
            self.rect.top = 5
        if self.rect.bottom >= Screen.HEIGHT-5:
            self.rect.bottom = Screen.HEIGHT-5