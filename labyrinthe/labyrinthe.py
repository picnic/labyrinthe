import time
from typing import List, Tuple


VIDE = 0
MUR = 1


class Labyrinthe(object):
    def __init__(self, cases: List[List[int]], affichage: bool = True, attente: float = 1):
        self._cases: List[List[int]] = cases
        self._affichage: bool = affichage
        self._attente: float = attente
        self._direction: Tuple[int, int] = (1, 0)
        self._position: Tuple[int, int] = (1, 1)
        self._largeur = len(self._cases[0])
        self._hauteur = len(self._cases)

    def avancer(self) -> None:
        (nx, ny) = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])
        if nx == -1 or ny == -1 or nx == self._largeur or ny == self._hauteur:
            print("Attention : tu es au bord du labyrinthe. Il faut utiliser la méthode sortir() !")
        elif self._cases[nx][ny] == MUR:
            print("Attention : tu as foncé dans un mur !")
        else:
            self._position = (nx, ny)
        if self._affichage:
            print(self._texte_labyrinthe())
        if self._attente > 0:
            time.sleep(self._attente)

    def tourner_a_gauche(self) -> None:
        self._direction = (self._direction[1], -self._direction[0])
        if self._affichage:
            print(self._texte_labyrinthe())
        if self._attente > 0:
            time.sleep(self._attente)


    def tourner_a_droite(self) -> None:
        self._direction = (-self._direction[1], self._direction[0])
        if self._affichage:
            print(self._texte_labyrinthe())
        if self._attente > 0:
            time.sleep(self._attente)

    def sortir(self) -> None:
        sur_un_bord = self._position[0] == 0 or self._position[0] == self._largeur - 1 or \
                      self._position[1] == 0 or self._position[1] == self._hauteur - 1
        if sur_un_bord:
            print("Bravo ! Vous avez réussi à sortir du labyrinthe ! :D")
        else:
            print("Rejoignez la sortie avant d’utiliser la méthode sortir() !")

    def obtenir_largeur(self) -> int:
        return self._largeur

    def obtenir_hauteur(self) -> int:
        return self._hauteur

    def obtenir_position(self) -> (int, int):
        return self._position

    def obtenir_direction(self) -> (int, int):
        return self._direction

    def _texte_labyrinthe(self) -> str:
        texte = ""
        for y, ligne in enumerate(self._cases):
            for x, case in enumerate(ligne):
                if case == MUR:
                    texte += "█"
                elif self._position == (x, y):
                    if self._direction == (1, 0):
                        texte += "→"
                    if self._direction == (-1, 0):
                        texte += "←"
                    if self._direction == (0, 1):
                        texte += "↓"
                    if self._direction == (0, -1):
                        texte += "↑"
                else:
                    texte += " "
            if y != self._hauteur - 1:
                texte += "\n"
        return texte
