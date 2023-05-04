import pygame
from parametres import *


class renderer:
    def __init__(self, jeu):
        self.jeu = jeu
        self.fenetre = self.jeu.fenetre
        self.mur = self.load()
        self.skybox = self.get_texture('textures/Lune.jpg', (xd, D_yd))
        self.skybox_offset = 0

    def draw(self):
        self.draw_skybox()
        self.render()

    def draw_skybox(self):
        self.skybox_offset = (self.skybox_offset + 4.0 * self.jeu.joueur.rel) % xd
        self.fenetre.blit(self.skybox, (-self.skybox_offset, 0))
        self.fenetre.blit(self.skybox, (-self.skybox_offset + xd, 0))

        pygame.draw.rect(self.fenetre, COULEUR_SOL, (0, D_yd, xd, yd))

    def render(self):
        liste_objets = sorted(self.jeu.raycasteur.pending, key = lambda t: t[0], reverse = True)
        for profondeur, image, pos in liste_objets:
            self.fenetre.blit(image, pos)

    @staticmethod
    def get_texture(chemin, res=(T_TEXTURE, T_TEXTURE)):
        texture = pygame.image.load(chemin).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load(self):
        return {
            1: self.get_texture('textures/1.png'),
            2: self.get_texture('textures/2.png'),             # Ici on ajoute les differentes textures de mur
        }
