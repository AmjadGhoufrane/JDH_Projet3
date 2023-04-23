import pygame
import sys
import math
from parametres import *
from carte import *
from joueur import *

pygame.init()


class Mainlanceur:
    def __init__(self, xd_lc, yd_lc):
        self.carte = Carte(self)
        self.joueur = Joueur(self)
        self.delta_time = 1
        self.fenetre = pygame.display.set_mode((xd_lc, yd_lc))
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
        self.joueur.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                self.continuer = False


Jeu = Mainlanceur(xd, yd)
while Jeu.continuer:
    Jeu.Main()
