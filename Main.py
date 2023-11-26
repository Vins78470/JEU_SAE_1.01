from Jeu import *
from Class import * 
# coding: utf-8




def main():
    coup_possible_coder = {'h': (-1, 0), 'b': (1, 0), 'g': (0, -1), 'd': (0, 1)}
    liste_symbole_missions = []
    liste_missions = []
    nb_joueur = 0
    liste_coder = []
    Board = []
  
    
    
    #while(GameIsOver(self) == False): # verifie si le joueur a les 5000 B
        
    Board = InitBoard(Board) #Initialise la board 21*21

    print("Bienvenue sur ESN Wars.")
    print("\n")
    nb_joueur = int(input(("A combien de joueur voulez vous jouer ? ")))

    if CheckNombreJoueur(nb_joueur):
        print("\n")

        liste_coder = InitialisationJoueur(Board,liste_coder,nb_joueur)
        liste_symbole_missions = GenerateSymbolMission(liste_symbole_missions)
        liste_missions = InitialisationMission(liste_missions,liste_symbole_missions)

        Board = DrawPlayerAtJobCenter(Board, liste_coder)
        Board = DrawMission(Board,liste_missions)

        PrintBoard(Board) # Affiche la Board 
    

        # Boucle pour que chaque joueur joue à tour de rôle

        for tour in range(1,500):  # Par exemple, 5 tours de 
            for coder in liste_coder:
                AfficherInfosMissions(liste_missions)
                print("--------------------------------------------------------------------------------------------------------------------")
                print("\n")
                AfficherInfosJoueur(liste_coder)

                print(f"Tour {tour}, Joueur {coder.GetSymbol()}")
                potential_position = input("Choisissez une case ou aller ( choix entre : h, b, g, d): ")
                if CheckDirectionInput(potential_position,coup_possible_coder):
                    potential_position = CherchePosition(potential_position,coup_possible_coder)
                    if IsMovable(potential_position,coder,liste_coder):
                        if IsCoderOnaMission(coder,liste_missions):
                            print("t'es sur une mission")
                        DeletePlayer(Board,coder)
                        DrawPlayer(Board,potential_position,coder)
                        UpdateJobCenter(Board, liste_coder)
                        PrintBoard(Board) # Affiche la Board
            
                        
    else:
        main()


main()


