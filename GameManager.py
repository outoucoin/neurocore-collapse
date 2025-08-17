import pygame
from MainMenu import MainMenu
from GamePlay import GamePlay

class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = 'main_menu'

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.current_screen == 'main_menu':
            self.current_screen = MainMenu(self.screen).run()  
        elif self.current_screen == 'game_play':
            self.current_screen = GamePlay(self.screen).run()

    def draw(self):
        pygame.display.flip()
        self.clock.tick(60)