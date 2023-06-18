import pygame

class Player:

    WIDTH = 10
    HEIGHT = 140
    COLOR = (255, 255, 255)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, Player.WIDTH, Player.HEIGHT)

    def draw(self, window):
        pygame.draw.rect(window, Player.COLOR, self.rect)
