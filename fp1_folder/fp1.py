from fp1_folder import fs11
from fp1_folder import fs12


def initialiser():
    coloniePresent = fs11.init_tab(25, 25)
    colonieFutur = fs11.init_tab(25, 25)

    coloniePresent = fs12.init_population(coloniePresent)
    return coloniePresent, colonieFutur
