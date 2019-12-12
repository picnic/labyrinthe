import unittest
from unittest.mock import patch, MagicMock

from labyrinthe import *


class TestLabyrinthe(unittest.TestCase):

    def setUp(self) -> None:
        self.cases = [[1, 1, 1, 1, 1],
                      [1, 0, 0, 1, 1],
                      [1, 0, 0, 1, 1],
                      [1, 0, 1, 1, 1]]
        self.laby = Labyrinthe(self.cases, affichage=False, attente=0)

    def test_constructeur(self) -> None:
        self.assertEqual(self.laby._cases, self.cases)
        self.assertEqual(self.laby._affichage, False)
        self.assertEqual(self.laby._affichage, False)
        self.assertEqual(self.laby._attente, 0)
        self.assertEqual(self.laby._position, (1, 1))
        self.assertEqual(self.laby._direction, (1, 0))

    @patch('builtins.print')
    @patch('time.sleep')
    def test_constructor_valeurs_par_defaut(self, sleep_mock: MagicMock, print_mock: MagicMock) -> None:
        laby = Labyrinthe(self.cases)
        self.assertEqual(laby._affichage, True)
        self.assertEqual(laby._attente, 1)

    @patch('labyrinthe.labyrinthe.Labyrinthe._texte_labyrinthe', return_value='fake')
    @patch('builtins.print')
    def test_constructor_avec_affichage(self, print_mock: MagicMock, texte_labyrinthe: MagicMock) -> None:
        Labyrinthe(self.cases, affichage=True, attente=0)
        texte_labyrinthe.assert_called_with()
        print_mock.assert_called_with('fake')

    @patch('builtins.print')
    def test_constructor_sans_affichage(self, print_mock: MagicMock) -> None:
        Labyrinthe(self.cases, affichage=False, attente=0)
        print_mock.assert_not_called()

    @patch('time.sleep')
    def test_constructor_avec_attente(self, sleep_mock: MagicMock) -> None:
        Labyrinthe(self.cases, affichage=False, attente=2)
        sleep_mock.assert_called_with(2)

    @patch('time.sleep')
    def test_constructor_sans_attente(self, sleep_mock: MagicMock) -> None:
        Labyrinthe(self.cases, affichage=False, attente=0)
        sleep_mock.assert_not_called()

    def test_avancer_vide(self) -> None:
        """Teste la méthode avancer dans les 4 directions vers une case vide"""
        self.laby._position = (1, 1)
        self.laby._direction = (1, 0)
        self.laby.avancer()
        self.assertEqual(self.laby._position, (2, 1))
        self.laby._position = (1, 1)
        self.laby._direction = (0, 1)
        self.laby.avancer()
        self.assertEqual(self.laby._position, (1, 2))
        self.laby._position = (2, 2)
        self.laby._direction = (0, -1)
        self.laby.avancer()
        self.assertEqual(self.laby._position, (2, 1))
        self.laby._position = (2, 2)
        self.laby._direction = (-1, 0)
        self.laby.avancer()
        self.assertEqual(self.laby._position, (1, 2))

    @patch('labyrinthe.labyrinthe.Labyrinthe._texte_labyrinthe', return_value='████\n█→ █\n█  █\n████')
    @patch('builtins.print')
    def test_avancer_avec_affichage(self, print_mock: MagicMock, texte_labyrinthe: MagicMock) -> None:
        self.laby._affichage = True
        self.laby.avancer()
        texte_labyrinthe.assert_called_with()
        print_mock.assert_called_with('████\n█→ █\n█  █\n████')

    @patch('builtins.print')
    def test_avancer_sans_affichage(self, print_mock: MagicMock) -> None:
        self.laby.avancer()
        print_mock.assert_not_called()

    @patch('time.sleep')
    def test_avancer_avec_attente(self, sleep_mock: MagicMock) -> None:
        self.laby._attente = 2.0
        self.laby.avancer()
        sleep_mock.assert_called_with(2.0)

    @patch('time.sleep')
    def test_avancer_sans_attente(self, sleep_mock: MagicMock) -> None:
        self.laby.avancer()
        sleep_mock.assert_not_called()

    @patch('builtins.print')
    def test_avancer_murs(self, print_mock: MagicMock) -> None:
        """Teste la méthode avancer dans les 4 directions vers une case mur"""
        self.laby._position = (2, 2)
        self.laby._direction = (1, 0)
        self.laby.avancer()
        print_mock.assert_called_with("Attention : tu as foncé dans un mur !")
        self.assertEqual(self.laby._position, (2, 2))
        self.laby._position = (2, 2)
        self.laby._direction = (0, 1)
        self.laby.avancer()
        print_mock.assert_called_with("Attention : tu as foncé dans un mur !")
        self.assertEqual(self.laby._position, (2, 2))
        self.laby._position = (1, 1)
        self.laby._direction = (0, -1)
        self.laby.avancer()
        print_mock.assert_called_with("Attention : tu as foncé dans un mur !")
        self.assertEqual(self.laby._position, (1, 1))
        self.laby._position = (1, 1)
        self.laby._direction = (-1, 0)
        self.laby.avancer()
        print_mock.assert_called_with("Attention : tu as foncé dans un mur !")
        self.assertEqual(self.laby._position, (1, 1))

    @patch('builtins.print')
    def test_avancer_bords(self, print_mock: MagicMock) -> None:
        """Teste la méthode avancer dans les 4 directions vers au bord du labyrinthe"""
        cases = [[0, 0],
                 [0, 0]]
        laby = Labyrinthe(cases, affichage=False, attente=0)

        laby._position = (1, 1)
        laby._direction = (1, 0)
        laby.avancer()
        print_mock.assert_called_with("Attention : tu es au bord du labyrinthe. Il faut utiliser la méthode sortir() !")
        self.assertEqual(laby._position, (1, 1))

        laby._position = (1, 1)
        laby._direction = (0, 1)
        laby.avancer()
        print_mock.assert_called_with("Attention : tu es au bord du labyrinthe. Il faut utiliser la méthode sortir() !")
        self.assertEqual(laby._position, (1, 1))

        laby._position = (0, 0)
        laby._direction = (0, -1)
        laby.avancer()
        print_mock.assert_called_with("Attention : tu es au bord du labyrinthe. Il faut utiliser la méthode sortir() !")
        self.assertEqual(laby._position, (0, 0))

        laby._position = (0, 0)
        laby._direction = (-1, 0)
        laby.avancer()
        print_mock.assert_called_with("Attention : tu es au bord du labyrinthe. Il faut utiliser la méthode sortir() !")
        self.assertEqual(laby._position, (0, 0))

    def test_tourner_a_gauche(self) -> None:
        """Teste la méthode tourner_a_gauche depuis les 4 directions"""
        self.laby._direction = (1, 0)
        self.laby.tourner_a_gauche()
        self.assertEqual(self.laby._direction, (0, -1))
        self.laby._direction = (0, -1)
        self.laby.tourner_a_gauche()
        self.assertEqual(self.laby._direction, (-1, 0))
        self.laby._direction = (-1, 0)
        self.laby.tourner_a_gauche()
        self.assertEqual(self.laby._direction, (0, 1))
        self.laby._direction = (0, 1)
        self.laby.tourner_a_gauche()
        self.assertEqual(self.laby._direction, (1, 0))

    @patch('labyrinthe.labyrinthe.Labyrinthe._texte_labyrinthe', return_value='fake')
    @patch('builtins.print')
    def test_tourner_a_gauche_avec_affichage(self, print_mock: MagicMock, texte_labyrinthe: MagicMock) -> None:
        self.laby._affichage = True
        self.laby.tourner_a_gauche()
        texte_labyrinthe.assert_called_with()
        print_mock.assert_called_with('fake')

    @patch('builtins.print')
    def test_tourner_a_gauche_sans_affichage(self, print_mock: MagicMock) -> None:
        self.laby.tourner_a_gauche()
        print_mock.assert_not_called()

    @patch('time.sleep')
    def test_tourner_a_gauche_avec_attente(self, sleep_mock: MagicMock) -> None:
        self.laby._attente = 2.0
        self.laby.tourner_a_gauche()
        sleep_mock.assert_called_with(2.0)

    @patch('time.sleep')
    def test_tourner_a_gauche_sans_attente(self, sleep_mock: MagicMock) -> None:
        self.laby.tourner_a_gauche()
        sleep_mock.assert_not_called()

    def test_tourner_a_droite(self) -> None:
        """Teste la méthode tourner_a_droite depuis les 4 directions"""
        self.laby._direction = (1, 0)
        self.laby.tourner_a_droite()
        self.assertEqual(self.laby._direction, (0, 1))
        self.laby._direction = (0, 1)
        self.laby.tourner_a_droite()
        self.assertEqual(self.laby._direction, (-1, 0))
        self.laby._direction = (-1, 0)
        self.laby.tourner_a_droite()
        self.assertEqual(self.laby._direction, (0, -1))
        self.laby._direction = (0, -1)
        self.laby.tourner_a_droite()
        self.assertEqual(self.laby._direction, (1, 0))

    @patch('labyrinthe.labyrinthe.Labyrinthe._texte_labyrinthe', return_value='fake')
    @patch('builtins.print')
    def test_tourner_a_droite_avec_affichage(self, print_mock: MagicMock, texte_labyrinthe: MagicMock) -> None:
        self.laby._affichage = True
        self.laby.tourner_a_droite()
        texte_labyrinthe.assert_called_with()
        print_mock.assert_called_with('fake')

    @patch('builtins.print')
    def test_tourner_a_droite_sans_affichage(self, print_mock: MagicMock) -> None:
        self.laby.tourner_a_droite()
        print_mock.assert_not_called()

    @patch('time.sleep')
    def test_tourner_a_droite_avec_attente(self, sleep_mock: MagicMock) -> None:
        self.laby._attente = 2.0
        self.laby.tourner_a_droite()
        sleep_mock.assert_called_with(2.0)

    @patch('time.sleep')
    def test_tourner_a_droite_sans_attente(self, sleep_mock: MagicMock) -> None:
        self.laby.tourner_a_droite()
        sleep_mock.assert_not_called()

    @patch('builtins.print')
    def test_sortir_bord(self, print_mock: MagicMock) -> None:
        self.laby._position = (1, 3)
        self.laby.sortir()
        print_mock.assert_called_with("Bravo ! Vous avez réussi à sortir du labyrinthe ! :D")

    @patch('builtins.print')
    def test_sortir_echec(self, print_mock: MagicMock) -> None:
        self.laby.sortir()
        print_mock.assert_called_with("Rejoignez la sortie avant d’utiliser la méthode sortir() !")

    def test_obtenir_largeur(self) -> None:
        self.assertEqual(self.laby.obtenir_largeur(), 5)

    def test_obtenir_hauteur(self) -> None:
        self.assertEqual(self.laby.obtenir_hauteur(), 4)

    def test_obtenir_position(self) -> None:
        self.assertEqual(self.laby.obtenir_position(), (1, 1))

    def test_obtenir_direction(self) -> None:
        self.assertEqual(self.laby.obtenir_direction(), (1, 0))

    def test_texte_labyrinthe_direction_droite(self) -> None:
        self.laby._direction = (1, 0)
        self.assertEqual(self.laby._texte_labyrinthe(), '█████\n█→ ██\n█  ██\n█ ███')

    def test_texte_labyrinthe_direction_gauche(self) -> None:
        self.laby._direction = (-1, 0)
        self.assertEqual(self.laby._texte_labyrinthe(), '█████\n█← ██\n█  ██\n█ ███')

    def test_texte_labyrinthe_direction_haut(self) -> None:
        self.laby._direction = (0, -1)
        self.assertEqual(self.laby._texte_labyrinthe(), '█████\n█↑ ██\n█  ██\n█ ███')

    def test_texte_labyrinthe_direction_bas(self) -> None:
        self.laby._direction = (0, 1)
        self.assertEqual(self.laby._texte_labyrinthe(), '█████\n█↓ ██\n█  ██\n█ ███')

    def test_regarder_a_gauche(self) -> None:
        self.laby._direction = (1, 0)
        self.laby._cases[0][1] = 2
        self.assertEqual(self.laby.regarder_a_gauche(), 2)
        self.laby._direction = (0, 1)
        self.laby._cases[1][2] = 3
        self.assertEqual(self.laby.regarder_a_gauche(), 3)
        self.laby._direction = (-1, 0)
        self.laby._cases[2][1] = 4
        self.assertEqual(self.laby.regarder_a_gauche(), 4)
        self.laby._direction = (0, -1)
        self.laby._cases[1][0] = 5
        self.assertEqual(self.laby.regarder_a_gauche(), 5)

    def test_regarder_a_droite(self):
        self.laby._direction = (1, 0)
        self.laby._cases[2][1] = 6
        self.assertEqual(self.laby.regarder_a_droite(), 6)
        self.laby._direction = (0, 1)
        self.laby._cases[1][0] = 7
        self.assertEqual(self.laby.regarder_a_droite(), 7)
        self.laby._direction = (-1, 0)
        self.laby._cases[0][1] = 8
        self.assertEqual(self.laby.regarder_a_droite(), 8)
        self.laby._direction = (0, -1)
        self.laby._cases[1][2] = 9
        self.assertEqual(self.laby.regarder_a_droite(), 9)

    def test_regarder_devant(self):
        self.laby._direction = (1, 0)
        self.laby._cases[1][2] = 6
        self.assertEqual(self.laby.regarder_devant(), 6)
        self.laby._direction = (0, 1)
        self.laby._cases[2][1] = 7
        self.assertEqual(self.laby.regarder_devant(), 7)
        self.laby._direction = (-1, 0)
        self.laby._cases[1][0] = 8
        self.assertEqual(self.laby.regarder_devant(), 8)
        self.laby._direction = (0, -1)
        self.laby._cases[0][1] = 9
        self.assertEqual(self.laby.regarder_devant(), 9)

    def test_regarder_a_gauche_bords(self) -> None:
        cases = [[0]]
        laby = Labyrinthe(cases, affichage=False, attente=0)
        laby._position = (0, 0)
        laby._direction = (1, 0)
        self.assertEqual(laby.regarder_a_gauche(), MUR)
        laby._direction = (0, 1)
        self.assertEqual(laby.regarder_a_gauche(), MUR)
        laby._direction = (-1, 0)
        self.assertEqual(laby.regarder_a_gauche(), MUR)
        laby._direction = (0, -1)
        self.assertEqual(laby.regarder_a_gauche(), MUR)

    def test_regarder_a_droite_bords(self) -> None:
        cases = [[0]]
        laby = Labyrinthe(cases, affichage=False, attente=0)
        laby._position = (0, 0)
        laby._direction = (1, 0)
        self.assertEqual(laby.regarder_a_droite(), MUR)
        laby._direction = (0, 1)
        self.assertEqual(laby.regarder_a_droite(), MUR)
        laby._direction = (-1, 0)
        self.assertEqual(laby.regarder_a_droite(), MUR)
        laby._direction = (0, -1)
        self.assertEqual(laby.regarder_a_droite(), MUR)

    def test_regarder_devant_bords(self) -> None:
        cases = [[0]]
        laby = Labyrinthe(cases, affichage=False, attente=0)
        laby._position = (0, 0)
        laby._direction = (1, 0)
        self.assertEqual(laby.regarder_devant(), MUR)
        laby._direction = (0, 1)
        self.assertEqual(laby.regarder_devant(), MUR)
        laby._direction = (-1, 0)
        self.assertEqual(laby.regarder_devant(), MUR)
        laby._direction = (0, -1)
        self.assertEqual(laby.regarder_devant(), MUR)
