from fp4_folder import fs41
from fp4_folder import fs42
from fp4_folder import fs43


def reinitialisation_colonie(population, oldPopulation, cptGenWithoutEvolve, coloniePresent, colonieFutur):
    run, cptGenWithoutEvolve = fs41.verification_fin_jeu(population, oldPopulation, cptGenWithoutEvolve)
    coloniePresent, colonieFutur = fs42.futur_devient_present(coloniePresent, colonieFutur)
    colonieFutur = fs43.reinitialisation_futur()
    return run, cptGenWithoutEvolve, coloniePresent, colonieFutur
