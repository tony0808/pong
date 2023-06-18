import pygame

class Screen:

    WIDTH = 1000
    HEIGHT = 700
    COLOR = (21, 12, 41)
    TITLE = 'PONG'

    def __init__(self):
        self.window = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
        pygame.display.set_caption(Screen.TITLE)