from asyncio.windows_events import NULL
import time


class Mission():
    
    def __init__(self,symbol, starting_workload, difficulty, position):
        
        """
        Initialise une mission avec les attributs spécifiés.

        Args:
        - symbol (str): Le symbole représentant la mission.
        - starting_workload (int): La charge de travail initiale de la mission.
        - difficulty (int): La difficulté de la mission.
        - position (tuple): La position de la mission sur le plateau.

        Attributes:
        - symbol (str): Le symbole représentant la mission.
        - starting_workload (int): La charge de travail initiale de la mission.
        - remaining_workload (int): La charge de travail restante de la mission.
        - difficulty (int): La difficulté de la mission.
        - position (tuple): La position de la mission sur le plateau.
        - unavailable_for_nb_round (int): Nombre de rounds où la mission est indisponible.
        """
        
        self.symbol = symbol
        self.starting_workload= starting_workload
        self.remaining_workload = starting_workload
        self.difficulty = difficulty             
        self.position = position
        self.unavailable_for_nb_round = 0  # Nombre de round pendant lesquels la mission sera indisponible
        
    
       # Valeurs initiales pour que quand la mission réapparaisse elle reprenne ses attributs
        self.symbole_initial = symbol
        self.starting_workload_initial = starting_workload
        self.remaining_workload_initial = starting_workload
        self.difficulty_initial = difficulty
        self.position_initial = position

 


    def GetSymbol(self):
        
        """
        Renvoie le symbole représentant la mission.

        Returns:
        - str: Le symbole représentant la mission.
        """
        return self.symbol

    def GetPosition(self):
        
        """
        Renvoie la position de la mission sur le plateau.

        Returns:
        - tuple: La position de la mission sur le plateau.
        """
        return self.position

    def GetStartingWorkLoad(self):
        """
        Renvoie la charge de travail initiale de la mission.

        Returns:
        - int: La charge de travail initiale de la mission.
        """
        return self.starting_workload
    
    def GetRemainingWorkLoad(self):
        
        """
        Renvoie la charge de travail restante de la mission.

        Returns:
        - int: La charge de travail restante de la mission.
        """
        return self.remaining_workload
       
    def GetDifficulty(self):
        """
        Renvoie la difficulté de la mission.

        Returns:
        - int: La difficulté de la mission.
        """
        return self.difficulty

    def rendre_indisponible(self, round):
        
        """
        Rend la mission indisponible pour un certain nombre de rounds.

        Args:
        - round (int): Le nombre de rounds pour lesquels la mission sera indisponible.
        """
        self.unavailable_for_nb_round = round
       
    
    def est_disponible(self):
        """
        Vérifie si la mission est disponible.

        Returns:
        - bool: True si la mission est disponible, sinon False.
        """
        return self.unavailable_for_nb_round == 0
    

    def decrementer_indisponibilite(self):
        """
        Diminue le temps d'indisponibilité de la mission d'un round s'il est supérieur à zéro.
        """
        if self.unavailable_for_nb_round > 0:
            self.unavailable_for_nb_round -= 1
            
    def RedrawAfterMissionNotAvailable(self,Board):
        """
        Redessine la mission sur le plateau après qu'elle soit de nouveau disponible.

        Args:
        - Board (list): Le plateau de jeu sur lequel redessiner la mission.
        """
        x,y = self.GetPosition()
        Board[x][y] = self.GetSymbol()
        

    def ResetValues(self):
        """
        Réinitialise les valeurs de la mission à leurs valeurs initiales.
        """
        self.symbol = self.symbole_initial
        self.starting_workload = self.starting_workload_initial
        self.remaining_workload = self.remaining_workload_initial
        self.difficulty = self.difficulty_initial
        self.position = self.position_initial
       
    
    def UpgradeRemainingWorkLoad(self, amount):
        """
        Met à jour la charge de travail restante de la mission.

        Args:
        - amount (int): La quantité à ajouter à la charge de travail restante.
        """
        if self.remaining_workload + amount >= 0:
            self.remaining_workload += amount
        else:
            # Si la soustraction donne une valeur négative, met à jour à 0
            self.remaining_workload = 0
    
    def ResetRemainingWorkLoad(self):
        """
        Réinitialise la charge de travail restante de la mission à zéro.
        """
        self.remaining_workload = 0


    
    


        




