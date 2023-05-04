from sprites import *


class npc(SpriteAnime):
    def __init__(self, jeu, chemin='textures/animes/1.png', pos=(10, 4.5), echelle=1.0, shift=0.0):
        super().__init__(jeu, chemin, pos, echelle, shift)
        self.jeu = jeu
        self.pos = pos
        self.chemin = chemin

