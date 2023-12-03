from tkinter import *
from Class import *


class WindowGame:

    def __init__(self, cell_size=50, nb_cell_width=21, nb_cell_height=21):
        self.CELL_SIZE = cell_size
        self.NB_CELL_WIDTH = nb_cell_width
        self.NB_CELL_HEIGHT = nb_cell_height
        self.WIDTH = self.CELL_SIZE * self.NB_CELL_WIDTH
        self.HEIGHT = self.CELL_SIZE * self.NB_CELL_HEIGHT


        self.fenetre = Tk()
        self.fenetre.title("ESN GAME")

        self.canvas = Canvas(self.fenetre, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()


        self.draw_board()  # Appel à la méthode draw_board() pour dessiner la grille dès la création de la fenêtre
         
        self.draw_joueur_at_center()
        self.canvas.bind_all('<KeyPress>', self.deplacer_joueur)

        self.fenetre.mainloop()
        

        
    # Draw initial rectangles
    def draw_board(self):
        for i in range(self.NB_CELL_HEIGHT):
            for j in range(self.NB_CELL_WIDTH):
                x1 = i * self.CELL_SIZE
                y1 = j * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')



    def draw_joueur_at_center(self):
        self.joueur = self.canvas.create_rectangle(
            self.WIDTH / 2 - self.CELL_SIZE / 2,
            self.HEIGHT / 2 - self.CELL_SIZE / 2,
            self.WIDTH / 2 + self.CELL_SIZE / 2,
            self.HEIGHT / 2 + self.CELL_SIZE / 2,
            fill="blue"
        )


    def draw_missions(self, liste_missions):
      
        for mission in liste_missions:
            mission_x, mission_y = mission.get_position()  # Utiliser le getter pour obtenir la position de la mission

            mission_x *= self.CELL_SIZE
            mission_y *= self.CELL_SIZE

            x1 = mission_x
            y1 = mission_y
            x2 = mission_x + self.CELL_SIZE
            y2 = mission_y + self.CELL_SIZE

            self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='yellow')

    def deplacer_joueur(self, event):
        touche = event.keysym
        if touche == "Up":
            self.canvas.move(self.joueur, 0, -self.CELL_SIZE)  # Déplacer vers le haut
        elif touche == "Down":
            self.canvas.move(self.joueur, 0, self.CELL_SIZE)  # Déplacer vers le bas
        elif touche == "Left":
            self.canvas.move(self.joueur, -self.CELL_SIZE, 0)  # Déplacer vers la gauche
        elif touche == "Right":
            self.canvas.move(self.joueur, self.CELL_SIZE, 0)  # Déplacer vers la droite


window = WindowGame()

