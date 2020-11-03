from fp3_folder import voisin
from fp3_folder.fs31_folder import fs313
from fp3_folder.fs31_folder import fs314


def determination_colonie_futur(coloniePresent, colonieFutur):
    for ligne in range(len(coloniePresent)):
        for column in range(len(coloniePresent[ligne])):
            # FS 3.1.1
            if ligne == 0 and column == 0:  # FS 3.1.1.1
                data = [[0, 1], [1, 0], [1, 1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)
            if ligne == (len(coloniePresent)-1) and column == 0:  # FS 3.1.1.2
                data = [[-1, 0], [-1, 1], [0, 1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)
            if ligne == 0 and column == (len(coloniePresent[ligne])-1) :  # FS 3.1.1.3
                data = [[0, -1], [1, -1], [1, 0]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)
            if ligne == (len(coloniePresent)-1) and column == (len(coloniePresent[ligne])-1) :  # FS 3.1.1.4
                data = [[-1, -1], [-1, 0], [0, -1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)

            # FS 3.1.2
            if column == 0 and (0 < ligne < len(coloniePresent)-1):  # FS 3.1.2.1
                data = [[-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)
            if (0 < column < len(coloniePresent[ligne])-1) and ligne == 0:  # FS 3.1.2.2
                data = [[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)
            if (0 < column < len(coloniePresent[ligne])-1) and (ligne == len(coloniePresent)-1):  # FS 3.1.2.3
                data = [[0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)
            if (column == len(coloniePresent[ligne])-1) and (0 < ligne < len(coloniePresent)-1):  # FS 3.1.2.4
                data = [[-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
                nbVoisin = voisin.determinationVoisin(coloniePresent, ligne, column, data)

            # FS 3.1.3
            if (0 < column < len(coloniePresent[ligne])-1) and (0 < ligne < len(coloniePresent)-1):
                nbVoisin = fs313.coin_inferieur_gauche(coloniePresent, ligne, column)

            colonieFutur[ligne][column] = fs314.statutFutureCellule(coloniePresent[ligne][column], nbVoisin)

    return coloniePresent, colonieFutur
