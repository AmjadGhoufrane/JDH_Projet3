import pygame
from parametres import *
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Boo:
    def __init__(self):
        pygame.mouse.set_visible(True)
        font = pygame.font.Font(None, 35)
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((xd,yd))
        pygame.mixer.music.load("boo.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.Main()
    def Main(self):
        bg = pygame.image.load("screamer.png")
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(bg,(xd,yd)),(0,0))
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                            pygame.quit()
                            sys.exit()