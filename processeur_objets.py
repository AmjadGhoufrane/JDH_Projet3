from sprites import *

# Ici on a notre classe qui permet de gerer nos sprites


class Processeur:
    def __init__(self, jeu):
        self.sprites = []
        self.jeu = jeu
        self.definition()

    def definition(self):
        self.sprites.append(SpriteAnime(self.jeu))          # ici on définit nos sprites en utilisant les classes qu'on a importé du fichier sprites
        self.sprites.append(Sprite(self.jeu))               # on utilise la syntaxe suivante self.sprites.append(Sprite(self.jeu, chemin, pos))

    def update(self):
        for sprite in self.sprites:
            sprite.update()
