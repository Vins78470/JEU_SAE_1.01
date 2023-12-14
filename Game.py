
# -*- coding: utf-8 -*-
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
        
    # Prend en argument la g�neration des symboles et par consequent son nombre de missions et cr�er des objets missions puis les mets dans une liste de mission


    def InitialisationMission(self):
        
        
        """
        Initialise les missions en creant des objets Mission et les ajoute a la liste des missions.
        Utilise les symboles et les parametres des missions provenant de la configuration.
        """

        for i in range(self.nb_de_mission):

             random_i = random.randint(1,20)
             random_j = random.randint(1,20)
             
            # Met a jour le fichier JSON pour que les param�tres des missions soit differents (�criture et lecture de fichier)
             self.configuration.UpdateFile()
          
             self.liste_missions.append(Mission(self.liste_symbole_missions[i], 
                                                self.configuration.starting_workload, 
                                                self.configuration.difficulty ,
                                                (random_i,random_j)))
  

    def InitialisationCoder(self):
        
        """
        Initialise les joueurs (coders) en creant des objets Coder et les ajoutant a la liste des coders.
        Utilise une liste predefinie de symboles pour les joueurs.
        """        
   
        liste_symbole_coder = ['P1','P2','P3','P4']
        
        
        for i in range(self.nb_coder):
             self.liste_coder.append(Coder(liste_symbole_coder[i],(10,10),1,1,1,0,"blue"))
    


    # Genere le nombre de missions qu'il y aura et cr�er des symboles pour ces missions

    def GenerateSymbolMission(self):
       
        # G�n�re les symboles pour les missions en fonction du nombre de missions defini.
        # Ces symboles sont crees sous la forme de 'M1', 'M2', ... jusqu'au nombre total de missions.
        # Les symboles sont stock�s dans la liste 'liste_symbole_missions'.
        for j in range (self.nb_de_mission):
            self.liste_symbole_missions.append("M"+str(j+1))


    def start(self):
        
        # D�marre le jeu.
        #- Initialise le plateau de jeu avec une taille de 21x21.
        #- V�rifie le nombre de joueurs pour le jeu.
        #- Initialise les joueurs et les missions.
        #- Affiche le plateau de jeu apr�s les initialisations.
        
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
            PrintBoard(self.Board)  # Affiche la Board dans la console apr�s les initialisations
            
        else:
            print(" Choisissez entre 1 et 4 joueurs : ")
            self.start()

    def play(self):
        
        # D�marre le d�roulement du jeu.
        # - Demande aux joueurs de se d�placer sur la carte et ex�cute les tours de jeu jusqu'� ce qu'un joueur atteigne les conditions de victoire.
        # - Affiche les informations sur les missions et les joueurs � chaque tour.
        # - V�rifie la validit� des mouvements saisis par les joueurs.
        # - V�rifie si un joueur a atteint les conditions de victoire � chaque tour.
        # - Affiche le r�sultat du jeu une fois termin�.
        
        while not self.isGameFinished:
            for round in range(1, 1001):  
                for coder in self.liste_coder:
                    print(AfficherInfosMissions(self.liste_missions))
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("\n")
                    print(AfficherInfosCoder(self.liste_coder))
                    print("--------------------------------------------------------------------------------------------------------------------")

                    print(f"Tour {round}, Coder {coder.GetSymbol()}")
                    
                    # Regarde si l'utilisateur a bien entr� une touche valide
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

                    if GameIsOver(coder) or coder.round == 10:
                        self.isGameFinished = True
                        break  # Sortir de la boucle des joueurs si un joueur a termin�
            
                if self.isGameFinished:
                    break  # Sortir de la boucle principale si un joueur a termin�
                
        # Utilisation de la fonction max avec une fonction de clé personnalisée pour obtenir le joueur avec le montant d'argent maximal
        joueur_gagnant = max(self.liste_coder, key=lambda joueur: joueur.GetMoneyAmount(), default=None)

        if self.isGameFinished:
            if joueur_gagnant is not None:
                # Vérifier s'il y a égalité
                gagnants = [j for j in self.liste_coder if j.GetMoneyAmount() == joueur_gagnant.GetMoneyAmount()]

                if len(gagnants) == 1:
                    print("\nLe jeu est fini. Le joueur " + str(joueur_gagnant.GetSymbol()) + " a gagné.\n")
                else:
                    print("\nÉgalité entre les joueurs:")
                    for gagnant in gagnants:
                        print("Joueur " + str(gagnant.GetSymbol()) + " a la même richesse maximale.")
                    print("\n")
            else:
                print("\nLa limite de tours est atteinte\n")



    def playOneRound(self, coder, move, round):
            
            # 
            # Effectue un tour de jeu pour un joueur.
            # 
            # Args:
            # - coder : Coder - Le joueur en action pour ce tour.
            # - move : tuple - La direction de mouvement choisie par le joueur.
            # - round : int - Le num�ro du tour actuel.

            # Actions :
            # - V�rifie si le mouvement est possible pour le joueur, le d�place sur la carte, met � jour son emplacement et l'affiche.
            # - V�rifie si le joueur est sur une mission et agit en cons�quence (d�pense d'�nergie, mise � jour de la mission, etc.).
            # - V�rifie et met � jour l'�nergie du joueur s'il est au centre.
            # - Actualise l'�tat des missions sur la carte.

            # Returns : None

        
            if IsMovable(move, coder, self.liste_coder):
                coder.round +=1
                print(coder.round)
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
            # => (dans ce cas on reset ces valeurs et on la redessine) si elle indisponible on d�cremente le compteur
            for mission in self.liste_missions:
                if mission.est_disponible() == False:
                    mission.decrementer_indisponibilite()
                    #mission.ResetValues()
                if mission.est_disponible():   
                        mission.RedrawAfterMissionNotAvailable(self.Board)

               
    def checkCoderEnergy(self, coder, round):
        
        # V�rifie l'�nergie du joueur au centre d'emploi et affiche un message s'il y est depuis un certain nombre de tours.

        # Args:
        # - coder : Coder - Le joueur dont l'�nergie est v�rifi�e.
        # - round : int - Le num�ro du tour actuel.

        # Actions :
        # - V�rifie si le joueur est au centre depuis un certain nombre de tours et affiche un message.

        # Returns : None
        # 
        if CheckJobCenter(self.Board, coder) and round >= 2:
            print("Vous etes bien sur le Job Center")
            print("\n")

      