import pygame

class Ball:

    WIDTH = 30
    HEIGHT = 30
    COLOR = (255, 255, 255)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, Ball.WIDTH, Ball.HEIGHT)
    
    def draw(self, window):
        pygame.draw.ellipse(window, Ball.COLOR, self.rect)