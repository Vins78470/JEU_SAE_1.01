

from Rules import *
from Coder import *
from Mission import *
from Configuration import *
import json

# -*- coding: utf-8 -*-

class Game():

    def __init__(self, nb_coder,level,nb_de_missions):
        
        self.nb_de_mission = nb_de_missions
        self.nb_coder = nb_coder
        self.configuration = Configuration(level)
        self.mission_supprime_a_check = 0
        self.compt = 0
        self.letter2MoveDictionnary = {'h': (-1, 0), 'b': (1, 0), 'g': (0, -1), 'd': (0, 1)}
        self.liste_symbole_missions = []
        self.liste_missions = []
        self.liste_coder = []
        self.Board = []
        self.isGameFinished = False
        
# Prend en argument la géneration des symboles et par consequent son nombre de missions et créer des objets missions puis les mets dans une liste de mission


    def InitialisationMission(self):

        for i in range(self.nb_de_mission):

             random_i = random.randint(1,20)
             random_j = random.randint(1,20)
             
            # Met a jour le fichier JSON pour que les paramètres des missions soit differents (écriture et lecture de fichier)
             self.configuration.UpdateFile()
          
             self.liste_missions.append(Mission(self.liste_symbole_missions[i], 
                                                self.configuration.starting_workload, 
                                                self.configuration.difficulty ,
                                                (random_i,random_j)))
  

    def InitialisationCoder(self):
   
        liste_symbole_coder = ['P1','P2','P3','P4']
        
        
        for i in range(self.nb_coder):
             self.liste_coder.append(Coder(liste_symbole_coder[i],(10,10),1,1,1,0,"blue"))
    


    # Genere le nombre de missions qu'il y aura et créer des symboles pour ces missions

    def GenerateSymbolMission(self):    
        for j in range (self.nb_de_mission):
            self.liste_symbole_missions.append("M"+str(j+1))


    def start(self):

        self.Board = InitBoard(self.Board)  # Initialise la board 21*21
        print(" Bienvenue sur ESN Wars ! ")
        print("\n")
   
        if CheckNombreCoder(self.nb_coder):
            print("\n")

            self.InitialisationCoder()
            self.GenerateSymbolMission()
            self.InitialisationMission()
            
            self.Board = DrawPlayerAtJobCenter(self.Board, self.liste_coder)
            self.Board = DrawMissions(self.Board, self.liste_missions)
            PrintBoard(self.Board)  # Affiche la Board dans la console après les initialisations
            
        else:
            print(" Choisissez entre 1 et 4 joueurs : ")
            self.start()

    def play(self):
        while not self.isGameFinished:
            for round in range(1, 500):  # Par exemple, 500 tours
                for coder in self.liste_coder:
                    print(AfficherInfosMissions(self.liste_missions))
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("\n")
                    print(AfficherInfosCoder(self.liste_coder))
                    print("--------------------------------------------------------------------------------------------------------------------")

                    print(f"Tour {round}, Coder {coder.GetSymbol()}")
                    
                    # Regarde si l'utilisateur a bien entré une touche valide
                    valid_letters = self.letter2MoveDictionnary.keys()
                    
                    moveLetter = input("Choisissez une case ou aller ( choix entre : h, b, g, d): ")

                    while moveLetter not in valid_letters:
                        print("\n")
                        print("Veuillez entrer une lettre valide.")
                        print("\n")
                        moveLetter = input("Choisissez une case ou aller ( choix entre : h, b, g, d): ")

                    print("\n")
                   
                    moveDirection = CherchePosition(moveLetter, self.letter2MoveDictionnary)

                    if CheckDirectionInput(moveLetter, self.letter2MoveDictionnary):
                        self.playOneRound(coder, moveDirection, round)

                    else:
                        print("Choisir une touche valide")

                    if GameIsOver(coder):
                        self.isGameFinished = True
                        break  # Sortir de la boucle des joueurs si un joueur a terminé
            
                if self.isGameFinished:
                    break  # Sortir de la boucle principale si un joueur a terminé

        if self.isGameFinished:
            print("\n")
            print("Le jeu est fini " + str(coder.GetSymbol()) + " a gagne ")
            print("\n")
        else:
            print("\n")
            print("La limite de tours est atteinte")
            print("\n")


    def playOneRound(self, coder, move, round):
            if IsMovable(move, coder, self.liste_coder):
                DeletePlayer(self.Board, coder)
                coder.MovePosition(move)
                DrawPlayer(self.Board, coder)
                UpdateJobCenter(self.Board, self.liste_coder)
                PrintBoard(self.Board)  # Affiche la Board
           
            mission_for_coder = FindMissionAssociatedToCoder(self.liste_missions,coder)
    
            if IsCoderOnaMission(coder, self.liste_missions):
                     
                  if mission_for_coder.est_disponible():
                        print("\n")
                        print(" Vous venez d'arrivez sur une mission ! ")
                        print("\n")
                        if EnoughEnergy(coder):
                            DepenseCoderEnergyPourLaMission(coder, self.liste_missions)
                            DepenseRwMission(coder, self.liste_missions)

                        if IsFinishMission(coder, self.liste_missions):
                            MissionIsFinishedYouWinMoney(coder, self.liste_missions)
                            mission_for_coder.rendre_indisponible(mission_for_coder.GetDifficulty()*10)
                        else:
                            ReDrawMission(self.Board, self.liste_missions, coder)
                     
                  else:
                      print(" Mission Non Disponible ! ")

            
            if CheckJobCenter(self.Board,coder) :
                self.checkCoderEnergy(coder, round)
            
            # On boucle sur la liste de mission pour voir si une mission est disponible
            # => (dans ce cas on reset ces valeurs et on la redessine) si elle indisponible on décremente le compteur
            for mission in self.liste_missions:
                if mission.est_disponible() == False:
                    mission.decrementer_indisponibilite()
                    #mission.ResetValues()
                if mission.est_disponible():   
                        mission.RedrawAfterMissionNotAvailable(self.Board)

               
    def checkCoderEnergy(self, coder, round):
        if CheckJobCenter(self.Board, coder) and round >= 2:
            print("Vous etes bien sur le Job Center")
            print("\n")

        #MakeChoiceAtJobCenter(coder, AskChoiceAtJobCenter())