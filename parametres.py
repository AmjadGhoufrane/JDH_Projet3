import math
import pygame
import sys

xd, yd = 1700, 900
FPS = 144
P_POS = 1.5, 6
P_ANGLE = 0
P_VITESSE = 0.04
P_VITESSE_ROTATION = 0.02
TAILLE_ECHELLE_JOUEUR = 5

MOUSE_SENSITIVITY = 0.002
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = xd - MOUSE_BORDER_LEFT

COULEUR_SOL = (70,70,70)

FOV = math.pi / 2  # FOV de 60°
D_FOV = FOV / 2
RAYONS = xd // 2
D_RAYONS = RAYONS // 2
D_xd = xd // 2
D_yd = yd // 2
DELTA_ANGLE = FOV / RAYONS
DRAW_DISTANCE = 50

DISTANCE_ECRAN = D_xd/math.tan(D_FOV)
ECHELLE = xd // RAYONS

T_TEXTURE = 256
D_T_TEXTURE = T_TEXTURE//2


class Parametres:
    def __init__(self):
        self.continuer = True
        font = pygame.font.Font(None, 48)
        self.clock = pygame.time.Clock()
        self.xd = xd
        self.yd = yd
        self.FPS = FPS
        self.FOV = FOV
        self.P_POS = P_POS
        self.P_ANGLE = P_ANGLE
        self.P_VITESSE = P_VITESSE
        self.P_VITESSE_ROTATION = P_VITESSE_ROTATION
        self.fov_text = font.render(f"FOV: {FOV}", True, (255, 255, 255))
        self.fps_text = font.render(f"FPS: {FPS}", True, (255, 255, 255))
        self.pos_text = font.render(f"P_POS: {P_POS}", True, (255, 255, 255))
        self.angle_text = font.render(f"P_ANGLE: {P_ANGLE}", True, (255, 255, 255))
        self.vitesse_text = font.render(f"P_VITESSE: {P_VITESSE}", True, (255, 255, 255))
        self.vitesse_rotation_text = font.render(f"P_VITESSE_ROTATION: {P_VITESSE_ROTATION}", True, (255, 255, 255))
        self.fov_rect = self.fov_text.get_rect(center=(xd // 2, yd // 2 - 144))
        self.fps_rect = self.fps_text.get_rect(center=(xd // 2, yd // 2 - 96))
        self.pos_rect = self.pos_text.get_rect(center=(xd // 2, yd // 2 - 48))
        self.angle_rect = self.angle_text.get_rect(center=(xd // 2, yd // 2))
        self.vitesse_rect = self.vitesse_text.get_rect(center=(xd // 2, yd // 2 + 48))
        self.vitesse_rotation_rect = self.vitesse_rotation_text.get_rect(center=(xd // 2, yd // 2 + 96))
        self.screen = pygame.display.set_mode((xd, yd))
        self.Main()

    def Main(self):
        bg = pygame.image.load("bg.png")
        self.clock.tick(FPS)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(bg,(xd,yd)),(0,0))
        self.screen.blit(self.fov_text, self.fov_rect)
        self.screen.blit(self.fps_text, self.fps_rect)
        self.screen.blit(self.pos_text, self.pos_rect)
        self.screen.blit(self.angle_text, self.angle_rect)
        self.screen.blit(self.vitesse_text, self.vitesse_rect)
        self.screen.blit(self.vitesse_rotation_text, self.vitesse_rotation_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                self.continuer = False
