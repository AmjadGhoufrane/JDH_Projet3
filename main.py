import pygame
import sys
import math
from parametres import *
from carte import *
from joueur import *
from raycaster import *
from pygame.locals import *
from creditss import * 

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

# Set up the display
screen = pygame.display.set_mode((xd,yd))
pygame.display.set_caption("The Dark Room")

pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Set up the font
font = pygame.font.Font(None, 48)

# Set up the "START" button
start_button_text = font.render("JOUER", True, (255, 255, 255))
start_button_rect = start_button_text.get_rect(center=(xd//2, yd//2+ 25))

# Set up the "SETTINGS" button
settings_button_text = font.render("PARAMETRES DU JEU", True, (255, 255, 255))
settings_button_rect = settings_button_text.get_rect(center=(xd//2, yd//2 + 100))

credits_button_text = font.render("CREDITS", True, (255, 255, 255))
credits_button_rect = credits_button_text.get_rect(center=(xd//2, yd//2 + 175))

quitter_button_text = font.render("QUITTER", True, (255, 255, 255))
quitter_button_rect = quitter_button_text.get_rect(center=(xd//2, yd//2 + 250))

f = pygame.font.Font(None, 100)
img=pygame.image.load("logo.png")

logo_button_text = f.render("LOGO TEMP", True, (255, 255, 255))
logo_button_rect = logo_button_text.get_rect(center=(xd//2, yd//2 -200))


class Mainlanceur:
    def __init__(self, xd_lc, yd_lc):
        self.carte = Carte(self)
        self.joueur = Joueur(self)
        self.raycasteur = raycasteur(self)
        self.delta_time = 1
        self.fenetre = pygame.display.set_mode((xd_lc, yd_lc))
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.map = Carte(self)
        self.Main()

    def Main(self):
        self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}')   # Permet d'afficher les fps en live à la place du nom de la fenetre
        self.fenetre.fill('black')
        #self.map.draw()
        self.raycasteur.update()
        self.joueur.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                self.continuer = False


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
            pygame.mixer.music.stop()
            # Launch the game
            Jeu = Mainlanceur(xd, yd)
            while Jeu.continuer:
                Jeu.Main()
        elif event.type == pygame.MOUSEBUTTONDOWN and settings_button_rect.collidepoint(event.pos):
            # Handle settings button click
            Parametre = Parametres()
            while Parametre.continuer:
                    Parametre.Main()
        elif event.type == pygame.MOUSEBUTTONDOWN and credits_button_rect.collidepoint(event.pos):
            credit = Credits()
            while credit.continuer :
                credit.Main()
        elif event.type == pygame.MOUSEBUTTONDOWN and quitter_button_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()
    # Center the text on the buttons
    start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
    settings_button_text_rect = settings_button_text.get_rect(center=settings_button_rect.center)

    # Draw the buttons
    screen.fill((0, 0, 0))
    screen.blit(start_button_text, start_button_text_rect)
    screen.blit(settings_button_text, settings_button_text_rect)
    screen.blit(credits_button_text, credits_button_rect)
    screen.blit(quitter_button_text, quitter_button_rect)
    screen.blit(pygame.transform.scale(img,(400,200)), logo_button_rect)
    
# Update the display
    pygame.display.flip()
