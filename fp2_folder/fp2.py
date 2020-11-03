import os


def affichage(coloniePresent, generation, population):
    os.system('cls')
    # for i in range(1, len(coloniePresent)-1):
    #     print(' '.join(coloniePresent[i][1:-1]))
    for i in range(len(coloniePresent)):
        print(' '.join(coloniePresent[i]))

    print(f"\nGénération : {generation}")
    print(f"Cellules : {population}")
