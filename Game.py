from Rules import *
from Class import *
import json
# -*- coding: utf-8 -*-

class Game():

    def __init__(self):

    
        self.mission_supprime_a_check = 0
        self.compt = 0
        self.letter2MoveDictionnary = {'h': (-1, 0), 'b': (1, 0), 'g': (0, -1), 'd': (0, 1)}
        self.liste_symbole_missions = []
        self.liste_missions = []
        self.nb_coder = 0
        self.liste_coder = []
        self.Board = []
        


    def start(self, nb_coder):

        self.Board = InitBoard(self.Board)  # Initialise la board 21*21
        print("Bienvenue sur ESN Wars.")
        print("\n")
        self.nb_coder = nb_coder

        if CheckNombreCoder(self.nb_coder):
            print("\n")

            self.liste_coder = InitialisationCoder(self.Board, self.liste_coder, self.nb_coder)
            self.liste_symbole_missions = GenerateSymbolMission(self.liste_symbole_missions)
            self.liste_missions = InitialisationMission(self.liste_missions, self.liste_symbole_missions)
            

            self.Board = DrawPlayerAtJobCenter(self.Board, self.liste_coder)
            self.Board = DrawMissions(self.Board, self.liste_missions)
            PrintBoard(self.Board)  # Affiche la Board dans la console après les initialisations
            
        else:
            print("Choisissez entre 1 et 4 joueurs")
            self.start(nb_coder)

    def play(self):
        for round in range(1, 500):  # Par exemple, 500 tours
            for coder in self.liste_coder:
                print(AfficherInfosMissions(self.liste_missions))
                print("--------------------------------------------------------------------------------------------------------------------")
                print("\n")
                print(AfficherInfosCoder(self.liste_coder))
                print("--------------------------------------------------------------------------------------------------------------------")

                print(f"Tour {round}, Coder {coder.GetSymbol()}")

                moveLetter = input("Choisissez une case ou aller ( choix entre : h, b, g, d): ")
                print("\n")
                moveDirection = CherchePosition(moveLetter, self.letter2MoveDictionnary)
                
                if CheckDirectionInput(moveLetter, self.letter2MoveDictionnary):
                    self.playRound(coder, moveDirection, round)
                    

                else:
                    print("choisir une touche valide")
             

    def playRound(self, coder, moveDirection,round):

            if IsMovable(moveDirection, coder, self.liste_coder):

                DeletePlayer(self.Board, coder)
                DrawPlayer(self.Board, moveDirection, coder)
                UpdateJobCenter(self.Board, self.liste_coder)
                PrintBoard(self.Board)  # Affiche la Board

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
                    UpdateMissions(self.liste_missions, self.mission_supprime_a_check)
            
            if CheckJobCenter(self.Board,coder) :
                self.checkCoderEnergy(coder,round)


    def checkCoderEnergy(self, coder, round):
        if CheckJobCenter(self.Board, coder) and round >= 2:
            print("Vous etes bien sur le JOB CENTER")
            print("\n")

        MakeChoiceAtJobCenter(coder, AskChoiceAtJobCenter())