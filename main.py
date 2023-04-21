import pygame
import sys
from parametres import *

pygame.init()


class Mainlanceur():
    def __init__(self, xd, yd):
        self.fenetre = pygame.display.set_mode((xd, yd))
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.Main()

    def Main(self):
        self.clock.tick(FPS)
        pygame.display.flip()
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                self.continuer = False
        self.fenetre.fill('black')


Jeu = Mainlanceur(xd, yd)
while Jeu.continuer:
    Jeu.Main()
