import pygame
from parametres import *
import math
import os
from fight import *
from collections import deque


class Sprite:
    def __init__(self, jeu, chemin='textures/sprites/arbre_1.png', pos=(10.5, 3.5), echelle=1.0, shift=0.0):
        self.sprite_d_xd = None
        self.dist = None
        self.norm_dist = None
        self.fenetre_x = None
        self.dx = None
        self.dy = None
        self.theta = None
        self.jeu = jeu
        self.joueur = jeu.joueur
        self.x, self.y = pos
        self.image = pygame.image.load(chemin).convert_alpha()
        self.xd_image = self.image.get_width()
        self.D_xd_image = self.image.get_width() // 2
        self.ratio_image = self.xd_image / self.image.get_height()
        self.echelle_sprite = echelle
        self.shift_sprite = shift

    def get_sprite_projection(self):
        proj = DISTANCE_ECRAN / self.norm_dist * self.echelle_sprite
        proj_xd, proj_yd = proj * self.ratio_image, proj

        image = pygame.transform.scale(self.image, (proj_xd, proj_yd))

        self.sprite_d_xd = proj_xd // 2
        shift_yd = proj_yd * self.shift_sprite
        pos = self.fenetre_x - self.sprite_d_xd, D_yd - proj_yd // 2 + shift_yd

        self.jeu.raycasteur.pending.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.joueur.x
        dy = self.y - self.joueur.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.joueur.angle
        if (dx > 0 and self.joueur.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rayons = delta / DELTA_ANGLE
        self.fenetre_x = (D_RAYONS + delta_rayons) * ECHELLE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.D_xd_image < self.fenetre_x < (xd + self.D_xd_image) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()


class SpriteAnime(Sprite):
    def __init__(self, jeu, chemin='textures/animes/1.png', pos=(10, 4.5), echelle=1.0, shift=0.0,
                 animation_time=120):
        super().__init__(jeu, chemin, pos, echelle, shift)
        self.animation_time = animation_time
        self.chemin = chemin.rsplit('/', 1)[0]
        self.images = self.get_images(self.chemin)
        self.animation_temps_precedant = pygame.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        if self.dx < 0 and self.dy < 0:
            Fight()
        else:
            if self.dx > 0:
                self.x -= 0.01
            elif self.dx < 0:
                self.x += 0.01
            if self.dy < 0:
                self.y += 0.01
            elif self.dy > 0:
                self.y -= 0.01
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pygame.time.get_ticks()
        if time_now - self.animation_temps_precedant > self.animation_time:
            self.animation_temps_precedant = time_now
            self.animation_trigger = True

    def get_images(self, chemin):
        images = deque()
        for file_name in os.listdir(chemin):
            if os.path.isfile(os.path.join(chemin, file_name)):
                img = pygame.image.load(chemin + '/' + file_name).convert_alpha()
                images.append(img)
        return images
