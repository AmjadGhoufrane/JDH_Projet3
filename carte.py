import pygame

_ = False


class Carte:
    def __init__(self, jeu):
        self.jeu = jeu
        self.carte = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, 1, 1, 2, 1, 1],
            [1, _, _, _, _, _, _, _, 1, 1, _, _, _, 1],
            [1, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, 2],
            [1, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, 1, 1, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, 1, 1, 2, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.carte_dict = {}
        self.get_map()

    def get_map(self):
        for y, ligne in enumerate(self.carte):
            for x, valeur in enumerate(ligne):
                if valeur:
                    self.carte_dict[(x, y)] = valeur  # permet de cataloguer les positions de toutes les paroies
        print(self.carte_dict)

    def draw(self):
        [pygame.draw.rect(self.jeu.fenetre, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.carte_dict]
