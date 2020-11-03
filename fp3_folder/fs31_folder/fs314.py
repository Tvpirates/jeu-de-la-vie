from function import other


def statutFutureCellule(cellule, voisin):
    if other.getEtat(cellule) and ((voisin == 2) or (voisin == 3)):
        return 'X'
    elif voisin == 3:
        return 'X'
    else:
        return ' '
