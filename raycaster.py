from parametres import *
from chargeur_textures import *
import math


class raycasteur:
    def __init__(self, jeu):
        self.jeu = jeu
        self.resultat = []
        self.pending = []
        self.textures = self.jeu.renderer.mur

    def get_object(self):
        self.pending = []
        for rayon, valeurs in enumerate(self.resultat):
            profondeur, hauteur_proj, texture, offset = valeurs
            if hauteur_proj < yd :
                colone = self.textures[texture].subsurface(
                    offset * (T_TEXTURE - ECHELLE), 0, ECHELLE, T_TEXTURE
                )
                colone = pygame.transform.scale(colone, (ECHELLE, hauteur_proj))
                mur_pos = (rayon * ECHELLE, D_yd - hauteur_proj // 2)
            else :
                hauteur_texture = T_TEXTURE * yd /hauteur_proj
                colone = self.textures[texture].subsurface(
                    offset*(T_TEXTURE-ECHELLE), D_T_TEXTURE - hauteur_texture //2,ECHELLE,hauteur_texture
                )
                colone = pygame.transform.scale(colone,(ECHELLE,yd))
                mur_pos = (rayon*ECHELLE,0)
            self.pending.append((profondeur, colone, mur_pos))

    def raycast(self):
        self.resultat = []
        ox, oy = self.jeu.joueur.pos
        x_carte, y_carte = self.jeu.joueur.case
        angle_rayon = self.jeu.joueur.angle - D_FOV + 0.0001
        texture_vert, texture_hor = 1, 1

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
                    texture_hor = self.jeu.carte.carte_dict[case_hor]
                    break
                x_hor += dx
                y_hor += dy
                profond_hor += delta_profondeur

            # calcul vertical
            x_vert, dx = (x_carte + 1, 1) if cos_a > 0 else (x_carte - 1e-6, -1)
            profond_vert = (x_vert - ox) / cos_a
            y_vert = oy + profond_vert * sin_a

            delta_profondeur = dx / cos_a
            dy = delta_profondeur * sin_a

            for i in range(DRAW_DISTANCE):
                case_vert = int(x_vert), int(y_vert)
                if case_vert in self.jeu.carte.carte_dict:
                    texture_vert = self.jeu.carte.carte_dict[case_vert]
                    break
                x_vert += dx
                y_vert += dy
                profond_vert += delta_profondeur

            # profondeur
            if profond_vert < profond_hor:
                profondeur, texture = profond_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1-y_vert)
            else:
                profondeur, texture = profond_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # anti fisheye
            # profondeur *= math.cos(self.jeu.joueur.angle - angle_rayon)

            # projction aka fausse 3d
            hauteur_proj = DISTANCE_ECRAN / (profondeur + 0.0001)

            # resultat
            self.resultat.append((profondeur, hauteur_proj, texture, offset))

            angle_rayon += DELTA_ANGLE

    def update(self):
        self.raycast()
        self.get_object()
