from joueur import *
from parametres import *
from carte import *
from chargeur_textures import *
import math


class raycasteur:
    def __init__(self, jeu):
        self.jeu = jeu

    def raycast(self):
        ox, oy = self.jeu.joueur.pos
        x_carte, y_carte = self.jeu.joueur.case
        angle_rayon = self.jeu.joueur.angle - D_FOV + 0.0001
        for rayon in range(RAYONS):
            sin_a = math.sin(angle_rayon)
            cos_a = math.cos(angle_rayon)

            # calcul horizental
            y_hor, dy = (y_carte + 1, 1) if sin_a > 0 else (y_carte - 1e-6, -1)
            profond_hor = (y_hor - oy) / sin_a
            x_hor = ox + profond_hor * cos_a

            delta_profondeur = dy / sin_a
            dx = delta_profondeur * cos_a

            for i in range(DRAW_DISTANCE):
                case_hor = int(x_hor), int(y_hor)
                if case_hor in self.jeu.carte.carte_dict:
                    break
                x_hor += dx
                y_hor += dy
                profond_hor += delta_profondeur

            # calcul vertical
            x_vert, dx = (x_carte + 1, 1) if cos_a > 0 else (x_carte * 1e-6, -1)
            profond_vert = (x_vert - ox) / cos_a
            y_vert = oy + profond_vert * sin_a

            delta_profondeur = dx / cos_a
            dy = delta_profondeur * sin_a

            for i in range(DRAW_DISTANCE):
                case_vert = int(x_vert), int(y_vert)
                if case_vert in self.jeu.carte.carte_dict:
                    break
                x_vert += dx
                y_vert += dy
                profond_vert += delta_profondeur

            # profondeur
            if profond_vert < profond_hor:
                profondeur = profond_vert
            else:
                profondeur = profond_hor

            # draw pour debug
            pygame.draw.line(self.jeu.fenetre, 'yellow', (100 * ox, 100 * oy),
                             (100 * ox + 100 * profondeur * cos_a, 100 * oy + 100 * profondeur * sin_a))

            angle_rayon += DELTA_ANGLE

    def update(self):
        self.raycast()
