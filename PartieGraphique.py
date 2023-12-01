from tkinter import *
from Jeu import DrawMissions


CELL_SIZE = 50
NB_CELL_WIDTH = 21
NB_CELL_HEIGHT = 21
WIDTH = CELL_SIZE*NB_CELL_WIDTH
HEIGHT = NB_CELL_HEIGHT * CELL_SIZE

fenetre = Tk()
fenetre.title("ESN GAME")


canvas = Canvas(fenetre, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_rectangle(1000, 0, CELL_SIZE, CELL_SIZE, outline='black', fill='white')


# Dessine une grille de cellules
for i in range(NB_CELL_HEIGHT):
    for j in range(NB_CELL_WIDTH):
        x1 = i * CELL_SIZE
        y1 = j * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')




# Dessine une grille de cellules
for i in range(NB_CELL_HEIGHT):
    for j in range(NB_CELL_WIDTH):
        x1 = i * CELL_SIZE
        y1 = j * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')

def DrawJoueurAtCenter(x,y):
     return canvas.create_rectangle(WIDTH/2 - CELL_SIZE / 2, HEIGHT/2 - CELL_SIZE / 2, WIDTH/2 + CELL_SIZE / 2, HEIGHT/2 + CELL_SIZE / 2, fill="blue")  # Création d'un joueur


joueur = DrawJoueurAtCenter(WIDTH/2,WIDTH/2)



def deplacer(event):
    touche = event.keysym
    if touche == "Up":
        canvas.move(joueur, 0, -CELL_SIZE)  # Déplacer vers le haut
    elif touche == "Down":
        canvas.move(joueur, 0, CELL_SIZE)  # Déplacer vers le bas
    elif touche == "Left":
        canvas.move(joueur, -CELL_SIZE, 0)  # Déplacer vers la gauche
    elif touche == "Right":
        canvas.move(joueur, CELL_SIZE, 0)  # Déplacer vers la droite



canvas.bind_all('<KeyPress>', deplacer )  # Lier la fonction de déplacement aux touches pressées

fenetre.mainloop()


from tkinter import *


