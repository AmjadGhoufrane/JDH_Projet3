from sprites import *

# Ici on a notre classe qui permet de gerer nos sprites


class Processeur:
    def __init__(self, jeu):
        self.sprites = []
        self.jeu = jeu
        self.definition()

    def definition(self):
        self.sprites.append(SpriteAnime(self.jeu,False,'textures/animes/1.png',(22.5,6.5)))          # ici on définit nos sprites en utilisant les classes qu'on a importé du fichier sprites
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/mort.png', (9.5, 11.5)))    # on utilise la syntaxe suivante self.sprites.append(Sprite(self.jeu, chemin, pos))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/mort.png', (8.5, 11.5)))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/mort.png', (7.5, 11.5)))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/mort.png', (6.5, 11.5)))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/mort.png', (5.5, 11.5)))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/mort.png', (4.5, 11.5)))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/table.png', (2, 8.5)))
        self.sprites.append(Sprite(self.jeu, 'textures/sprites/table.png', (2, 11.5)))

    def update(self):
        for sprite in self.sprites:
            sprite.update()
