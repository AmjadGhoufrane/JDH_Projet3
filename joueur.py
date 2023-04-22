from parametres import *
import math
import pygame


class Joueur:
    def __init__(self, jeu):
        self.jeu = jeu
        self.angle = P_ANGLE
        self.x, self.y = P_POS

    def mouvement(self):
        pass

    def update(self):
        self.mouvement()
