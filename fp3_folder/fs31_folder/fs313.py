from function import other


def coin_inferieur_gauche(coloniePresent, ligne, column):
    nbVoisin = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if not (a == 0 and b == 0) and other.getEtat(coloniePresent[ligne+a][column+b]):
                nbVoisin += 1

    return nbVoisin
