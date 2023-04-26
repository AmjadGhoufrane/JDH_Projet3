import pygame
from parametres import *


class renderer:
    def __init__(self, jeu):
        self.jeu = jeu
        self.fenetre = self.jeu.fenetre
        self.mur = self.load()

    def draw(self):
        self.render()

    def render(self):
        liste_objets = self.jeu.raycasteur.pending
        for profondeur, image, pos in liste_objets:
            self.fenetre.blit(image, pos)

    @staticmethod
    def get_texture(chemin, res=(T_TEXTURE, T_TEXTURE)):
        texture = pygame.image.load(chemin).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load(self):
        return {
            1: self.get_texture('textures/1.png'),
            2: self.get_texture('textures/2.png')
        }
