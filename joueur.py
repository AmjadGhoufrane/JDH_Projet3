from parametres import *
import math
import pygame


class Joueur:
    def __init__(self, jeu):
        self.rel = None
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

        self.check_wall_collision(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= P_VITESSE_ROTATION * self.jeu.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += P_VITESSE_ROTATION * self.jeu.delta_time
        self.angle %= math.tau

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([D_xd, D_yd])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.jeu.delta_time

    def check_wall(self, x, y):
        return (x, y) not in self.jeu.carte.carte_dict

    def check_wall_collision(self, dx, dy):
        scale = TAILLE_ECHELLE_JOUEUR / self.jeu.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        #pygame.draw.line(self.jeu.fenetre, 'yellow', ((self.x * 100)/5, (self.y * 100)/5),
        #                 ((self.x * 100)/5 + (xd/5) * math.cos(self.angle),
        #                  (self.y * 100)/5 + (xd/5) * math.sin(self.angle)), 2)
        pygame.draw.circle(self.jeu.fenetre, 'green', ((self.x * 100)/5, (self.y * 100)/5), 6)

    def update(self):
        self.mouvement()
        self.mouse_control()
        self.draw()

    @property  # Permet de recuperer la position comme une variable mais avec un intermediaire
    def pos(self):
        return self.x, self.y

    @property
    def case(self):
        return int(self.x), int(self.y)
