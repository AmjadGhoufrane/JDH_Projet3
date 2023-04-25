from parametres import *
import math
import pygame


class Joueur:
    def __init__(self, jeu):
        self.jeu = jeu
        self.angle = P_ANGLE
        self.x, self.y = P_POS

    def mouvement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = P_VITESSE * self.jeu.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        num_key_pressed = -1

        if keys[pygame.K_z]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_q]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos
        if self.collisions(int(self.x + dx), int(self.y + dy)):
            self.x += dx
            self.y += dy

        if keys[pygame.K_LEFT]:
            self.angle -= P_VITESSE_ROTATION * self.jeu.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += P_VITESSE_ROTATION * self.jeu.delta_time

    def collisions(self, x, y):
        return (x, y) not in self.jeu.carte.carte_dict

    def draw(self):
        #pygame.draw.line(self.jeu.fenetre, 'yellow', (self.x * 100, self.y * 100),
        #                 (self.x * 100 + xd * math.cos(self.angle),
        #                  self.y * 100 + xd * math.sin(self.angle)), 2)
        pygame.draw.circle(self.jeu.fenetre, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.mouvement()
        self.draw()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def case(self):
        return int(self.x), int(self.y)
