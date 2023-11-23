from Jeu import AfficherInfosJoueur, DrawPlayer, GameIsOver,InitBoard,PrintBoard,InitialisationJoueur
from Class import * 



def main():
    
    nb_joueur = 0
    liste_coder = []
    nb_joueur = 0 
    Board = []
    nb_joueur = 0
    
    
    #while(GameIsOver(self) == False): # verifie si le joueur a les 5000 B
        
    Board = InitBoard(Board) #Initialise la board 21*21

    print("Bienvenue sur ESN Wars.")
    print("\n")
    nb_joueur = int(input(("A combien de joueur voulez vous jouer ? ")))
    print("\n")
    liste_coder = InitialisationJoueur(Board,liste_coder,nb_joueur)
    AfficherInfosJoueur(liste_coder)
    Board = DrawPlayer(Board,liste_coder)
    PrintBoard(Board) # Affiche la Board 



main()


