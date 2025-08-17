import pygame
from Player import Player

class GamePlay:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()

    def run(self):
        playing = True
        while playing:
            self.handle_events()
            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
        return 'main_menu'

    def handle_events(self):
        self.player.handle_input()

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        pygame.display.flip()