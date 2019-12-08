import random
from typing import List
from labyrinthe.labyrinthe import MUR, VIDE

class Case:
    """
    Classe pour stocker l’état des murs qui entourent une case.

    Attributes:
        mur_gauche (bool): Y a t-il un mur à gauche de la case.
        mur_droit (bool): Y a t-il un mur à droite de la case.
        mur_haut (bool): Y a t-il un mur en haut de la case.
        mur_bas (bool): Y a t-il un mur en bas de la case.
    """

    def __init__(self, gauche=True, droit=True, haut=True, bas=True):
        """
        Constructeur pour Case.

        Parameters:
            gauche (bool): True s’il y a un mur à gauche.
            droit (bool): True s’il y a un mur à droite.
            haut (bool): True s’il y a un mur en haut.
            bas (bool): True s’il y a un mur en bas.
        """
        self.mur_gauche = gauche
        self.mur_droit = droit
        self.mur_haut = haut
        self.mur_bas = bas


def _trouver_voisins_non_visites(labyrinthe, position, cases_visitees):
    voisins_non_visites = []
    if position[0] > 0 and (position[0] - 1, position[1]) not in cases_visitees:
        voisins_non_visites.append((position[0] - 1, position[1]))
    if position[0] < len(labyrinthe[0]) - 1 and (position[0] + 1, position[1]) not in cases_visitees:
        voisins_non_visites.append((position[0] + 1, position[1]))
    if position[1] > 0 and (position[0], position[1] - 1) not in cases_visitees:
        voisins_non_visites.append((position[0], position[1] - 1))
    if position[1] < len(labyrinthe) - 1 and (position[0], position[1] + 1) not in cases_visitees:
        voisins_non_visites.append((position[0], position[1] + 1))
    return voisins_non_visites


def _supprimer_murs(labyrinthe, position1, position2):
    if position1[0] == position2[0]:
        if position1[1] > position2[1]:
            position1, position2 = position2, position1
        labyrinthe[position1[1]][position1[0]].mur_bas = False
        labyrinthe[position2[1]][position2[0]].mur_haut = False
    else:
        if position1[0] > position2[0]:
            position1, position2 = position2, position1
        labyrinthe[position1[1]][position1[0]].mur_droit = False
        labyrinthe[position2[1]][position2[0]].mur_gauche = False


def generer_labyrinthe_aleatoire(largeur: int, hauteur: int) -> List[List[Case]]:
    """
    Genere un labyrinthe sous la forme d’une liste de liste de cases.

    Parameters:
        largeur (int): number of columns (> 0)
        hauteur (int): number of rows (> 0)

    Returns:
        list[list[Case]]: Labyrinthe parfait généré de taille largeur x hauteur.
    """
    random.seed()
    labyrinthe = [[Case() for j in range(largeur)] for i in range(hauteur)]
    cases_visitees = set()
    pile_de_cases = []
    case_courante = (0, 0)
    cases_visitees.add(case_courante)
    while len(cases_visitees) < largeur * hauteur:
        voisins_non_visites = _trouver_voisins_non_visites(labyrinthe, case_courante, cases_visitees)
        if voisins_non_visites:
            case_suivante = random.choice(voisins_non_visites)
            pile_de_cases.append(case_courante)
            _supprimer_murs(labyrinthe, case_courante, case_suivante)
            case_courante = case_suivante
            cases_visitees.add(case_courante)
        elif pile_de_cases:
            case_courante = pile_de_cases.pop()
    labyrinthe[hauteur - 1][largeur - 2].mur_bas = False
    return labyrinthe


def convertir_labyrinthe(labyrinthe: List[List[Case]]) -> List[List[int]]:
    """
    Transforme un labyrinthe représenté par des cases en labyrinthe représenté par des entiers.
    Les dimensions du résultat par rapport à l’argument sont égales à (largeur * 2 + 1, hauteur * 2 + 1)

    Parameters:
        labyrinthe (List[List[Case]]): Labyrinthe sous forme de cases.

    Returns:
        List[List[int]]: Labyrinthe sous forme d’entiers.
    """
    resultat = []
    res_ligne = [MUR]
    for case in labyrinthe[0]:
        res_ligne.append(MUR if case.mur_haut else VIDE)
        res_ligne.append(MUR)
    resultat.append(res_ligne)
    for ligne in labyrinthe:
        res_ligne = [MUR if ligne[0].mur_gauche else VIDE]
        for case in ligne:
            res_ligne.append(VIDE)
            res_ligne.append(MUR if case.mur_droit else VIDE)
        resultat.append(res_ligne)
        res_ligne = [MUR]
        for case in ligne:
            res_ligne.append(MUR if case.mur_bas else VIDE)
            res_ligne.append(MUR)
        resultat.append(res_ligne)
    return resultat
