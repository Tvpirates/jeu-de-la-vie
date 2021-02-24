import pygame

from gamefile.gameclass.game.case import Case

class GameGrille:
    def __init__(self, taille, ligne, title="Grille de jeu"):
        self.title = title
        self.width = taille
        self.rows = ligne

        # Couleurs
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (128, 128, 128)

        self.win = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_caption(self.title)

    def makeGrid(self):
        """
        Création de la grille de jeu
        """
        self.grid = []
        gap = self.width // self.rows
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                spot = Case(i, j, gap, self.rows, self.white)
                self.grid[i].append(spot)

    def getXY(self):
        gap = self.width // self.rows
        a, b = self.pos

        self.y = a // gap
        self.x = b // gap

    def actionClickDroit(self):
        print(f"Clic droit {self.pos}, {self.x}, {self.y}")

    def actionClickGauche(self):
        print(f"Clic gauche {self.pos}, {self.x}, {self.y}")

    def show(self):
        self.win.fill(self.white)

        for row in self.grid:
            for case in row:
                case.draw(self.win)

        self.showGrid()
        pygame.display.update()

    def showGrid(self):
        gap = self.width // self.rows
        for i in range(self.rows):
            pygame.draw.line(self.win, self.grey, (0, i * gap), (self.width, i * gap))
            for j in range(self.rows):
                pygame.draw.line(self.win, self.grey, (j * gap, 0), (j * gap, self.width))

    def run(self):
        self.makeGrid()
        self.win.fill(self.white)

        isRunning = True
        self.isCalculing = False
        while isRunning:
            self.show()

            # Liste de tous les évènements
            for event in pygame.event.get():

                # clic sur la croix
                if event.type == pygame.QUIT:
                    print("on quitte le jeu")
                    isRunning = False

                # Clic Gauche souris
                if pygame.mouse.get_pressed()[0]:
                    self.pos = pygame.mouse.get_pos() # Récupération de la position
                    self.getXY()
                    self.actionClickGauche()


                # Clic Droit souris
                if pygame.mouse.get_pressed()[2]:
                    self.pos = pygame.mouse.get_pos() # Récupération de la position
                    self.getXY()
                    self.actionClickDroit()

                # Add for the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.actionClickSpaceBar()
                    if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.reset()
                    if event.key == pygame.K_KP_ENTER and not self.isCalculing:
                        self.aleatoireComplete()

if __name__ == '__main__':
    game = GameGrille(800, 10)

    game.run()
