from gamefile.gameclass.game.gamegrille import GameGrille

import pygame
import time
from random import seed, random

# On refait appel à notre class principale
class Grille(GameGrille):
    def __init__(self, taille, ligne, title="Le jeu de la vie"):
        super(Grille, self).__init__(taille, ligne, title)

        self.speed = 0.05

    def actionClickDroit(self):
        cell = self.grid[self.y][self.x]
        cell.becomeDeath(self.white)

    def actionClickGauche(self):
        cell = self.grid[self.y][self.x]
        cell.becomeAlive(self.black)

    def reset(self):
        pygame.display.set_caption(self.title)
        for ligne in range(len(self.grid)):
            for column in range(len(self.grid[ligne])):
                cell = self.grid[ligne][column]
                cell.status = False
                cell.futurStatustatus = False
                cell.color = self.white

    def aleatoireComplete(self):
        seed(1)

        for ligne in range(len(self.grid)):
            for column in range(len(self.grid[ligne])):
                if int(random()*100) < 30:
                    cell = self.grid[ligne][column]
                    cell.becomeAlive(self.black)

    def updateSpeed(self, action):
        if not action: # On augmente la vitesse
            self.speed += 0.1
            if self.speed > 1:
                self.speed = 1
        else:
            self.speed -= 0.1
            if self.speed < 0:
                self.speed = 0

    def actionClickSpaceBar(self):
        pygame.display.set_caption(f"{self.title} - Run")
        self.isCalculing = True
        while self.isCalculing:
            self.show()

            self.calculPosition()
            self.actualiseCell()

            time.sleep(self.speed)

            # Capture des évènements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isCalculing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.isCalculing = False
                    if event.key == pygame.K_KP_PLUS:
                        self.updateSpeed(True)
                    if event.key == pygame.K_KP_MINUS:
                        self.updateSpeed(False)

        pygame.display.set_caption(f"{self.title} - Stop")

    def isActive(self, ligne, column, a, b):
        return self.grid[ligne+a][column+b].status

    def actualiseCell(self):
        for ligne in range(len(self.grid)):
            for column in range(len(self.grid[ligne])):
                actCell = self.grid[ligne][column]
                actCell.status = actCell.futurStatus
                if actCell.status:
                    actCell.becomeAlive(self.black)
                else:
                    actCell.becomeDeath(self.white)

    def calculPosition(self):
        for ligne in range(len(self.grid)):
            for column in range(len(self.grid[ligne])):
                actCell = self.grid[ligne][column]
                actCell.nbVoisin = 0
                # Cas spéciaux, les coins
                if ligne == 0 and column == 0:  # En haut à gauche
                    if self.isActive(ligne, column, 0, 1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 1):
                        actCell.nbVoisin += 1

                if ligne == (len(self.grid)-1) and column == 0:  # En bas à gauche
                    if self.isActive(ligne, column, -1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, 1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 0, 1):
                        actCell.nbVoisin += 1

                if ligne == 0 and column == (len(self.grid[ligne])-1) :  # En haut à droite
                    if self.isActive(ligne, column, 0, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 0):
                        actCell.nbVoisin += 1

                if ligne == (len(self.grid)-1) and column == (len(self.grid[ligne])-1) :  # En bas à droite
                    if self.isActive(ligne, column, -1, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 0, -1):
                        actCell.nbVoisin += 1

                # Cas Spéciaux, les bors sans les coins
                if column == 0 and (0 < ligne < len(self.grid)-1):  # Bords Gauche
                    if self.isActive(ligne, column, -1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, 1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 0, 1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 1):
                        actCell.nbVoisin += 1

                if (0 < column < len(self.grid[ligne])-1) and ligne == 0:  # Bords Haut
                    if self.isActive(ligne, column, 0, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 0, 1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 1):
                        actCell.nbVoisin += 1

                if (0 < column < len(self.grid[ligne])-1) and (0 < ligne < len(self.grid)-1):  # Bords Bas
                    if self.isActive(ligne, column, 0, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 0, 1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, 1):
                        actCell.nbVoisin += 1

                if (column == len(self.grid[ligne])-1) and (0 < ligne < len(self.grid)-1):  # Bords Droit
                    if self.isActive(ligne, column, -1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, 0):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, -1, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 0, -1):
                        actCell.nbVoisin += 1
                    if self.isActive(ligne, column, 1, -1):
                        actCell.nbVoisin += 1

                # Autres cellules
                if (0 < column < len(self.grid[ligne])-1) and (0 < ligne < len(self.grid)-1):
                    actCell.nbVoisin = 0
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if not (a == 0 and b == 0) and self.isActive(ligne, column, a, b):
                                actCell.nbVoisin += 1

                if actCell.status:
                    if (actCell.nbVoisin == 2) or (actCell.nbVoisin == 3):
                        actCell.futurStatus = True
                    else:
                        actCell.futurStatus = False
                else:
                    if actCell.nbVoisin == 3:
                        actCell.futurStatus = True
                    else:
                        actCell.futurStatus = False

def main():
    game = Grille(800, 50)

    game.run()
