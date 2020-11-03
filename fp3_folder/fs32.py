from function import other


def comptage_cellules(colonieFutur):
    population = 0
    for ligne in range(len(colonieFutur)):
        for column in range(len(colonieFutur[ligne])):
            if other.getEtat(colonieFutur[ligne][column]):
                population += 1
    return population
