from Jeu import *
from Class import * 
import os
import json



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
        Board = DrawMissions(Board,liste_missions)

        PrintBoard(Board) # Affiche la Board 
    

        for tour in range(1,500):  # Par exemple, 500 tours 
            for coder in liste_coder:
                AfficherInfosMissions(liste_missions)
                print("--------------------------------------------------------------------------------------------------------------------")
                print("\n")
                AfficherInfosJoueur(liste_coder)
                print("--------------------------------------------------------------------------------------------------------------------")
                if CheckJobCenter(Board,coder) and tour >= 2:
                        print("Vous etes bien sur le JOB CENTER")
                        print("\n")
                        MakeChoiceAtJobCenter(coder,liste_missions)
                        
                if IsCoderOnaMission(coder,liste_missions):
                    print("t'es sur une mission")

                    if EnoughEnergy(coder):
                            DepenseCoderEnergyPourLaMission(coder,liste_missions)
                            DepenseRwMission(coder,liste_missions)

                    if IsFinishMission(coder,liste_missions):
                            MissionIsFinishedYouWinMoney(coder,liste_missions)
                            #DeleteMission(liste_missions, coder)
                            UpdateMissions(coder,liste_missions, tour)
                    else:
                       ReDrawMission(Board,liste_missions,coder)


     

                print(f"Tour {tour}, Joueur {coder.GetSymbol()}")
                
                potential_position = input("Choisissez une case ou aller ( choix entre : h, b, g, d): ")
                print("\n")
                           
                if CheckDirectionInput(potential_position,coup_possible_coder):

                    potential_position = CherchePosition(potential_position,coup_possible_coder)
                                
                    if IsMovable(potential_position,coder,liste_coder):

                        DeletePlayer(Board,coder)
                        DrawPlayer(Board,potential_position,coder)
                        UpdateJobCenter(Board, liste_coder)
                        PrintBoard(Board) # Affiche la Board
            
                        
    else:
        main()


main()


