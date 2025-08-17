import pygame
from GameManager import GameManager

def main():
    # Initialiser Pygame
    pygame.init()
    # Cr�er un objet GameManager
    game_manager = GameManager()
    # Lancer le jeu
    game_manager.run()

if __name__ == '__main__':
    main()