from sprites import *


# def __init__(self, jeu, chemin='textures/sprites/arbre_1.png', pos=(10.5, 3.5), echelle=1.0, shift=0.0):

class Processeur:
    def __init__(self, jeu):
        self.sprites = []
        self.jeu = jeu
        self.definition()

    def definition(self):
        self.sprites.append(SpriteAnime(self.jeu))
        self.sprites.append(Sprite(self.jeu))

    def update(self):
        for sprite in self.sprites:
            sprite.update()
