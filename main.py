import time

# Import des fonction FP et FS
from fp1_folder import fp1
from fp2_folder import fp2
from fp3_folder import fp3
from fp4_folder import fp4


start = input("Appuyer sur Enter pour démarrer !")

# Initialisation des variables
coloniePresent, colonieFutur = fp1.initialiser()
generation = 0
population = 0
oldPopulation = 0
cptGenWithoutEvolve = 0
run = True
while run:
    generation += 1
    fp2.affichage(coloniePresent, generation, population)
    oldPopulation = population
    population, coloniePresent, colonieFutur = fp3.evolution_population(coloniePresent, colonieFutur)
    run, cptGenWithoutEvolve, coloniePresent, colonieFutur = fp4.reinitialisation_colonie(population, oldPopulation, cptGenWithoutEvolve, coloniePresent, colonieFutur)
    time.sleep(0.2)
