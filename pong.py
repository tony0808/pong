import pygame, sys
from player import Player
from screen import Screen
from ball import Ball

class Pong:

    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def start(self):
        pygame.init()
        self.create_players()
        self.create_ball()
        self.run_game_loop()
        pygame.quit()

    def create_ball(self):
        x = (Screen.WIDTH - Ball.WIDTH) / 2
        y = (Screen.HEIGHT - Ball.HEIGHT) / 2
        self.ball = Ball(x, y)

    def create_players(self):
        self.create_left_player()
        self.create_right_player()

    def create_left_player(self):
        x = Player.WIDTH
        y = (Screen.HEIGHT-Player.HEIGHT)/2
        self.left_player = Player(x, y)

    def create_right_player(self):
        x = Screen.WIDTH-2*Player.WIDTH
        y = (Screen.HEIGHT-Player.HEIGHT)/2
        self.right_player = Player(x, y)

    def run_game_loop(self):
        while self.running:
            self.handle_events()
            self.draw_and_update_window()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def draw_and_update_window(self):
        self.draw_window()
        self.update_window()

    def draw_window(self):
        self.screen.window.fill(Screen.COLOR)
        self.left_player.draw(self.screen.window)
        self.right_player.draw(self.screen.window)
        self.ball.draw(self.screen.window)
        pygame.draw.aaline(self.screen.window, (255, 255, 255), (Screen.WIDTH/2, 0), (Screen.WIDTH/2, Screen.HEIGHT))

    def update_window(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)