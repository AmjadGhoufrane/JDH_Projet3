import pygame
from parametres import *
class Secret:
    def __init__(self):
        font = pygame.font.Font(None, 35)
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.text = font.render("hehe", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(xd//2, yd//2))
        self.screen = pygame.display.set_mode((xd,yd))
        self.Main()
    def Main(self):
        bg = pygame.image.load("bg.png")
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(bg,(xd,yd)),(0,0))
        self.screen.blit(self.text, self.text_rect)
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                            self.continuer = False