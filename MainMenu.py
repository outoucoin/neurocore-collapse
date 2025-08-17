import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.title = self.font.render('NEUROCORE: Collapse', True, (255, 0, 0))
        self.play_button = self.font.render('Jouer', True, (0, 255, 0))

    def run(self):
        menu_open = True
        while menu_open:
            self.screen.fill((0, 0, 0))  
            self.screen.blit(self.title, (150, 100))
            self.screen.blit(self.play_button, (250, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_open = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu_open = False  # Quitter le menu pour commencer le jeu
                        return 'game_play'  
        return 'main_menu'