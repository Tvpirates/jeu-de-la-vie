from fp3_folder import fs31
from fp3_folder import fs32


def evolution_population(coloniePresent, colonieFutur):
    coloniePresent, colonieFutur = fs31.determination_colonie_futur(coloniePresent, colonieFutur)
    population = fs32.comptage_cellules(colonieFutur)

    return population, coloniePresent, colonieFutur
