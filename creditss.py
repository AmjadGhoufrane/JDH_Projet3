import pygame
from parametres import *
class Credits :
    def __init__(self):
        font = pygame.font.Font(None, 35)
        font1 = pygame.font.Font(None, 48)
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.codeurs = font1.render("Jeu crée par : Jalal, Amjad, Youssef et Shireen. Logo fait par Maria Sefiani", True, (255, 255, 255))
        self.principe1 =  font.render("Dans ""The Darkness"", le joueur doit non seulement trouver un moyen de sortir de la maison hantée,", True, (255, 255, 255))
        self.bis1 = font.render("mais également survivre aux attaques répétées d'un fantôme maléfique qui apparaît lors de vagues de plus en plus difficiles à surmonter. ", True, (255, 255, 255))
        self.principe2 = font.render("Le joueur doit explorer la maison à la recherche d'indices sur la façon de ", True, (255, 255, 255))
        self.bis2 = font.render("vaincre le fantôme tout en évitant ses attaques et en essayant de rester en vie.", True, (255, 255, 255))
        self.principe3 = font.render("Le jeu mettra à l'épreuve les compétences de survie et d'énigmes du joueur,", True, (255, 255, 255))
        self.principe4 = font.render(" tout en créant une atmosphère effrayante et angoissante pour une expérience de jeu d'horreur immersive.", True, (255, 255, 255))
        self.codeurs_rect = self.codeurs.get_rect(center=(xd//2, yd//2 - 128))
        self.principe_rect1 = self.principe1.get_rect(center=(xd//2, yd//2-35))
        self.bis_rect1 = self.bis1.get_rect(center=(xd//2, yd//2))
        self.principe_rect2 = self.principe2.get_rect(center=(xd//2, yd//2 + 35))
        self.bis_rect2 = self.bis2.get_rect(center=(xd//2, yd//2+70))
        self.principe_rect3 = self.principe3.get_rect(center=(xd//2, yd//2 + 105))
        self.principe_rect4 = self.principe4.get_rect(center=(xd//2, yd//2 + 140))
        self.screen = pygame.display.set_mode((xd,yd))
        self.Main()
    def Main(self):
        bg = pygame.image.load("bg.png")
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(bg,(xd,yd)),(0,0))
        self.screen.blit(self.principe1, self.principe_rect1)
        self.screen.blit(self.principe2, self.principe_rect2)
        self.screen.blit(self.principe3, self.principe_rect3)
        self.screen.blit(self.principe4, self.principe_rect4)
        self.screen.blit(self.bis1, self.bis_rect1)
        self.screen.blit(self.bis2, self.bis_rect2)
        self.screen.blit(self.codeurs, self.codeurs_rect)
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                            self.continuer = False