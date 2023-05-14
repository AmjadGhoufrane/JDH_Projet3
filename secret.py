import pygame
from parametres import *
from pygame.locals import *
from boo import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Secret:
    def __init__(self):
        pygame.mouse.set_visible(True)
        font = pygame.font.Font(None, 48)
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.text = font.render("Felcitations, vous avez fini le jeu...", True, (255, 255, 255))
        self.text2 = font.render("Cliquez pour continuer", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(xd//2 -20, yd//2))
        self.text2_rect = self.text.get_rect(center=(xd//2 + 80, yd//2+50))
        self.screen = pygame.display.set_mode((xd,yd))
        pygame.mixer.music.load("ending.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.Main()
    def Main(self):
        bg = pygame.image.load("bg.png")
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(bg,(xd,yd)),(0,0))
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text2, self.text2_rect)
        
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and self.text2_rect.collidepoint(event.pos):
                            pygame.mixer.music.stop()
                            hehe = Boo()
                            while hehe.continuer:
                                hehe.Main()