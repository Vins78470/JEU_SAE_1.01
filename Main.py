from Jeu import *
from Class import * 

nb_joueur = 0 
Board = []

def main(joueur1,mission1):
    global Board
    global nb_joueur
    
    while(GameIsOver(joueur1) == False): # verifie si le joueur a les 5000 B
        Board = InitBoard(Board) #Initialise la board 21*21
        PrintBoard(Board) # Affiche la Board    

        print("Bienvenue sur ESN Wars.")
        nb_joueur = int(input(("A combien de joueur voulez vous jouer ? ")))




joueur1 = Coder(1,1,1,1,1)
mission1 = Mission(2,1,5)

main(joueur1,mission1)


