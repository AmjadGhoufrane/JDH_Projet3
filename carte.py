class Carte:
    def __init__(self):
        self.carte = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],  # Ici on dessine la carte du jeu, la plus part des implementation sur
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],  # internet utilisent soit des dictionaires de string ou des listes de liste
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # ici on le fait avec une liste de liste afin de simplifier notre raycasting
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def position(self, x, y):
        if self.carte[x][y] == 0:
            return self.carte[x][y], False
        return self.carte[x][y], True


