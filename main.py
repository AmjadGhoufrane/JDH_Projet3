import pygame
import sys
import math
from parametres import *
from carte import *

pygame.init()


class Mainlanceur:
    def __init__(self, xd, yd):
        self.fenetre = pygame.display.set_mode((xd, yd))
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.map = Carte(self)
        self.Main()

    def Main(self):
        self.clock.tick(FPS)
        pygame.display.flip()
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}')   # Permet d'afficher les fps en live à la place du nom de la fenetre
        self.fenetre.fill('black')
        self.map.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                self.continuer = False


Jeu = Mainlanceur(xd, yd)
while Jeu.continuer:
    Jeu.Main()
