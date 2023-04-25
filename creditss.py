import pygame
from parametres import *
class Credits :
    def __init__(self):
        font = pygame.font.Font(None, 48)
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.codeurs = font.render("Jeu crée par : Jalal, Amjad, Youssef et Shireen", True, (255, 255, 255))
        self.principe =  font.render("PlaceHolder pour le principe du jeu", True, (255, 255, 255))
        self.codeurs_rect = self.codeurs.get_rect(center=(xd//2, yd//2 - 50))
        self.principe_rect = self.principe.get_rect(center=(xd//2, yd//2))
        self.screen = pygame.display.set_mode((xd,yd))
        self.Main()
    def Main(self):
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.principe, self.principe_rect)
        self.screen.blit(self.codeurs, self.codeurs_rect)
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                            self.continuer = False