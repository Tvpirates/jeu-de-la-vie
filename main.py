import os
import time


def initColonie(coloniePresent):
    # coloniePresent[ligne][colonne]
    coloniePresent[1][4] = 'X'
    coloniePresent[2][4] = 'X'
    coloniePresent[3][4] = 'X'

    coloniePresent[0][10] = 'X'
    coloniePresent[0][11] = 'X'
    coloniePresent[0][12] = 'X'

    coloniePresent[8][11] = 'X'
    coloniePresent[9][12] = 'X'
    coloniePresent[9][13] = 'X'
    coloniePresent[10][11] = 'X'
    coloniePresent[10][10] = 'X'

    coloniePresent[12][4] = 'X'
    coloniePresent[12][5] = 'X'
    coloniePresent[13][4] = 'X'
    coloniePresent[13][6] = 'X'
    coloniePresent[14][5] = 'X'
    coloniePresent[14][6] = 'X'
    coloniePresent[14][7] = 'X'
    coloniePresent[15][6] = 'X'
    coloniePresent[15][7] = 'X'
    coloniePresent[15][8] = 'X'
    coloniePresent[16][5] = 'X'
    coloniePresent[16][6] = 'X'
    coloniePresent[16][7] = 'X'
    coloniePresent[17][6] = 'X'
    coloniePresent[17][4] = 'X'
    coloniePresent[18][4] = 'X'
    coloniePresent[18][5] = 'X'

    return coloniePresent


def initcoloniePresent(x, y):
    coloniePresent = [[' ']*(y) for k in range(x)]
    return coloniePresent


def affichageTableau(coloniePresent):
    os.system('cls')
    # for i in range(1, len(coloniePresent)-1):
    #     print(' '.join(coloniePresent[i][1:-1]))
    for i in range(len(coloniePresent)):
        print(' '.join(coloniePresent[i]))


def evolutionPopulation(coloniePresent):
    colonieFutur = initcoloniePresent(len(coloniePresent), len(coloniePresent[0]))
    for ligne in range(len(coloniePresent)):
        for column in range(len(coloniePresent[ligne])):
            # Cas Spéciaux, les coins
            if ligne == 0 and column == 0:  # En haut à gauche
                data = [[0, 1], [1, 0], [1, 1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)
            if ligne == (len(coloniePresent)-1) and column == 0:  # En bas à gauche
                data = [[-1, 0], [-1, 1], [0, 1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)
            if ligne == 0 and column == (len(coloniePresent[ligne])-1) :  # En haut à droite
                data = [[0, -1], [1, -1], [1, 0]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)
            if ligne == (len(coloniePresent)-1) and column == (len(coloniePresent[ligne])-1) :  # En bas à droite
                data = [[-1, -1], [-1, 0], [0, -1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)

            # Cas Spéciaux, les bors sans les coins
            if column == 0 and (0 < ligne < len(coloniePresent)-1):  # Bords Gauche
                data = [[-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)
            if (0 < column < len(coloniePresent[ligne])-1) and ligne == 0:  # Bords Haut
                data = [[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)
            if (0 < column < len(coloniePresent[ligne])-1) and (ligne == len(coloniePresent)-1):  # Bords Bas
                data = [[0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)
            if (column == len(coloniePresent[ligne])-1) and (0 < ligne < len(coloniePresent)-1):  # Bords Droit
                data = [[-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
                nbVoisin = determinationVoisin(coloniePresent, ligne, column, data)

            # Autres cellules
            if (0 < column < len(coloniePresent[ligne])-1) and (0 < ligne < len(coloniePresent)-1):
                nbVoisin = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if not (a == 0 and b == 0) and getEtat(coloniePresent[ligne+a][column+b]):
                            nbVoisin += 1

            colonieFutur[ligne][column] = statutFutureCellule(coloniePresent[ligne][column], nbVoisin)

    del coloniePresent

    return colonieFutur, calculPopulation(colonieFutur)


def determinationVoisin(colonie, x, y, data):
    nbVoisin = 0
    for d in data:
        if getEtat(colonie[x + d[0]][y + d[1]]):
            nbVoisin += 1
    return nbVoisin


def statutFutureCellule(cellule, voisin):
    if getEtat(cellule) and ((voisin == 2) or (voisin == 3)):
        return 'X'
    elif voisin == 3:
        return 'X'
    else:
        return ' '


def calculPopulation(colonieFutur):
    pop = 0
    for ligne in range(len(colonieFutur)):
        for column in range(len(colonieFutur[ligne])):
            if getEtat(coloniePresent[ligne][column]):
                pop += 1
    return pop


def getEtat(Cellule):
    if Cellule == 'X':
        return True
    else:
        return False


if __name__ == '__main__':
    start = input("Appuyer sur Enter pour démarrer !")
    coloniePresent = initcoloniePresent(20, 20)
    coloniePresent = initColonie(coloniePresent)
    generation = 1
    population = 0
    while True:
        affichageTableau(coloniePresent)
        print(f"\nGénération : {generation}")
        print(f"Cellules : {population}")
        generation += 1
        coloniePresent, population = evolutionPopulation(coloniePresent)
        time.sleep(0.2)
