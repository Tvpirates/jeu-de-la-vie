def verification_fin_jeu(population, oldPopulation, cptGenWithoutEvolve):
    if population == 0 or cptGenWithoutEvolve == 10:
        run = False
    else:
        run = True

    if oldPopulation == population:
        cptGenWithoutEvolve += 1
    else:
        cptGenWithoutEvolve = 0

    return run, cptGenWithoutEvolve
