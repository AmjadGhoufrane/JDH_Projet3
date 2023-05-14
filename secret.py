import pygame
from parametres import *
from pygame.locals import *
from boo import *
from creditss import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Secret:
    def __init__(self):
        pygame.mouse.set_visible(True)
        font = pygame.font.Font(None, 48)
        font1 = pygame.font.Font(None, 300)
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.text = font1.render("GAME OVER...", True, (255, 255, 255))
        self.text2 = font.render("Cliquez pour continuer", True, (255, 255, 255))
        self.text3 = font.render("Crédits", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(xd//2, yd//2 - 100))
        self.text2_rect = self.text2.get_rect(center=(xd//2, yd//2 + 50))
        self.text3_rect = self.text3.get_rect(center=(xd//2, yd//2+100))
        self.screen = pygame.display.set_mode((xd,yd))
        pygame.mixer.music.load("ending.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.Main()
    def Main(self):
        bg = pygame.image.load("arriere.png")
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(bg,(xd,yd)),(0,0))
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text2, self.text2_rect)
        self.screen.blit(self.text3, self.text3_rect)
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and self.text2_rect.collidepoint(event.pos):
                            pygame.mixer.music.stop()
                            hehe = Boo()
                            while hehe.continuer:
                                hehe.Main()
                        elif event.type == pygame.MOUSEBUTTONDOWN and self.text3_rect.collidepoint(event.pos):
                            pygame.mixer.music.stop()
                            hehe = Credits()
                            while hehe.continuer:
                                hehe.Main()