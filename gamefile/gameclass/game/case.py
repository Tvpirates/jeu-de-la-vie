import pygame

class Case:
    def  __init__(self, row, col, width, total_rows, couleur):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = couleur
        self.width = width
        self.total_rows = total_rows

        self.status = False # True => Alive and False => death
        self.nbVoisin = 0
        self.futurStatus = False # True => Alive and False => death

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def becomeDeath(self, color):
        self.status = False
        self.color = color

    def becomeAlive(self, color):
        self.status = True
        self.color = color
