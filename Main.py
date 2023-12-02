from Jeu import *
from Class import *
from PartieGraphique import *
import os
import json

class Game(GameWindow):

    def __init__(self, cell_size=50, nb_cell_width=21, nb_cell_height=21):
        super().__init__(cell_size, nb_cell_width, nb_cell_height)
        self.mission_supprime_a_check = 0
        self.compt = 0
        self.coup_possible_coder = {'h': (-1, 0), 'b': (1, 0), 'g': (0, -1), 'd': (0, 1)}
        self.liste_symbole_missions = []
        self.liste_missions = []
        self.nb_joueur = 0
        self.liste_coder = []
        self.Board = []

    def initialize_game(self):
        self.Board = InitBoard(self.Board)  # Initialise la board 21*21
        print("Bienvenue sur ESN Wars.")
        print("\n")
        self.nb_joueur = int(input(("A combien de joueur(s) voulez vous jouer ? ")))

        if CheckNombreJoueur(self.nb_joueur):
            print("\n")

            self.liste_coder = InitialisationJoueur(self.Board, self.liste_coder, self.nb_joueur)
            self.liste_symbole_missions = GenerateSymbolMission(self.liste_symbole_missions)
            self.liste_missions = InitialisationMission(self.liste_missions, self.liste_symbole_missions)

            self.Board = DrawPlayerAtJobCenter(self.Board, self.liste_coder)
            self.Board = DrawMissions(self.Board, self.liste_missions)

            PrintBoard(self.Board)  # Affiche la Board dans la console
            self.draw_board()  # Affiche la Board

            # Convertir les objets Mission en objets Coder pour utiliser les getters
            mission_positions = [(mission.GetPosition()) for mission in self.liste_missions]
            self.draw_missions(mission_positions)  # Dessiner les missions

            self.play_game()

        else:
            self.initialize_game()

    def play_game(self):
        for tour in range(1, 500):  # Par exemple, 500 tours
            for coder in self.liste_coder:
                AfficherInfosMissions(self.liste_missions)
                print("--------------------------------------------------------------------------------------------------------------------")
                print("\n")
                AfficherInfosJoueur(self.liste_coder)
                print("--------------------------------------------------------------------------------------------------------------------")

                print(f"Tour {tour}, Joueur {coder.GetSymbol()}")

                potential_position = input("Choisissez une case ou aller ( choix entre : h, b, g, d): ")
                print("\n")

                if CheckDirectionInput(potential_position, self.coup_possible_coder):

                    potential_position = CherchePosition(potential_position, self.coup_possible_coder)

                    if IsMovable(potential_position, coder, self.liste_coder):

                        DeletePlayer(self.Board, coder)
                        DrawPlayer(self.Board, potential_position, coder)
                        UpdateJobCenter(self.Board, self.liste_coder)
                        PrintBoard(self.Board)  # Affiche la Board

                if CheckJobCenter(self.Board, coder) and tour >= 2:
                    print("Vous etes bien sur le JOB CENTER")
                    print("\n")
                    MakeChoiceAtJobCenter(coder, self.liste_missions)

                if IsCoderOnaMission(coder, self.liste_missions):
                    print("t'es sur une mission")

                    if EnoughEnergy(coder):
                        DepenseCoderEnergyPourLaMission(coder, self.liste_missions)
                        DepenseRwMission(coder, self.liste_missions)

                    if IsFinishMission(coder, self.liste_missions):
                        MissionIsFinishedYouWinMoney(coder, self.liste_missions)
                        self.mission_supprime_a_check = DeleteMission(self.liste_missions, coder)
                    else:
                        ReDrawMission(self.Board, self.liste_missions, coder)
                        self.compt += 1

                if self.mission_supprime_a_check != 0:
                    if CheckReapparitionMission(self.compt, self.mission_supprime_a_check):
                        print("c congru")
                        UpdateMissions(self.liste_missions, self.mission_supprime_a_check)


game = Game()
game.initialize_game()
