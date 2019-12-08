import unittest
from labyrinthe import generer_labyrinthe_aleatoire, Case, convertir_labyrinthe
from typing import List, Tuple


class TestGenerateur(unittest.TestCase):
    def test_generer_labyrinthe_aleatoire_11(self) -> None:
        labyrinthe = generer_labyrinthe_aleatoire(1, 1)
        self.assertTrue(labyrinthe[0][0].mur_gauche)
        self.assertTrue(labyrinthe[0][0].mur_droit)
        self.assertTrue(labyrinthe[0][0].mur_haut)
        self.assertFalse(labyrinthe[0][0].mur_bas)

    def _trouver_cases_a_visiter(self, labyrinthe: List[List[Case]], position: Tuple[int, int]) -> List[Tuple[int, int]]:
        cases_a_visiter = []
        if not labyrinthe[position[1]][position[0]].mur_gauche and position[0] != 0:
            cases_a_visiter.append((position[0] - 1, position[1]))
        if not labyrinthe[position[1]][position[0]].mur_droit and position[0] != len(labyrinthe[0]) - 1:
            cases_a_visiter.append((position[0] + 1, position[1]))
        if not labyrinthe[position[1]][position[0]].mur_haut and position[1] != 0:
            cases_a_visiter.append((position[0], position[1] - 1))
        if not labyrinthe[position[1]][position[0]].mur_bas and position[1] != len(labyrinthe) - 1:
            cases_a_visiter.append((position[0], position[1] + 1))
        return cases_a_visiter

    def test_generer_labyrinthe_aleatoire(self) -> None:
        labyrinthe = generer_labyrinthe_aleatoire(10, 5)
        self.assertEqual(len(labyrinthe), 5)
        self.assertEqual(len(labyrinthe[0]), 10)

        # On essaie d’atteindre toutes les cases pour vérifier que le labyrinthe est généré correctement
        sorties = set()
        cases_visitees = set()
        pile_de_cases = [(0, 0)]
        while len(pile_de_cases):
            position = pile_de_cases.pop()
            if position not in cases_visitees:
                cases_visitees.add(position)
                if position[0] == 0 and not labyrinthe[position[1]][position[0]].mur_gauche:
                    sorties.add(position)
                if position[0] == 9 and not labyrinthe[position[1]][position[0]].mur_droit:
                    sorties.add(position)
                if position[1] == 0 and not labyrinthe[position[1]][position[0]].mur_haut:
                    sorties.add(position)
                if position[1] == 4 and not labyrinthe[position[1]][position[0]].mur_bas:
                    sorties.add(position)
                pile_de_cases = pile_de_cases + self._trouver_cases_a_visiter(labyrinthe, position)
        self.assertEqual(len(cases_visitees), 10 * 5)
        self.assertEqual(len(sorties), 1)

    def test_convertir_labyrinthe(self) -> None:
        laby_cases = [
            [Case(True, False, True, True), Case(False, True, True, False)],
            [Case(True, False, True, False), Case(False, True, False, True)],
        ]
        labyrinthe = convertir_labyrinthe(laby_cases)
        laby_attendu = [[1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1],
                        [1, 1, 1, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 0, 1, 1, 1]]
        self.assertEqual(labyrinthe, laby_attendu)
