from function import other


def determinationVoisin(colonie, x, y, data):
    nbVoisin = 0
    for d in data:
        if other.getEtat(colonie[x + d[0]][y + d[1]]):
            nbVoisin += 1
    return nbVoisin
