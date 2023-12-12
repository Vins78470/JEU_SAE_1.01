from asyncio.windows_events import NULL
import time
# -*- coding: utf-8 -*-


class Coder():
    """
    Représente un joueur (coder) dans le jeu.

    Attributes:
    - s (str): Symbole du joueur.
    - p (tuple): Position du joueur sur la carte.
    - cl (int): Niveau de codage du joueur.
    - em (int): Énergie maximale du joueur.
    - e (int): Énergie actuelle du joueur.
    - r (int): Montant d'argent du joueur.
    - color (str): Couleur du joueur.
    - rect (object): Rectangle pour l'affichage graphique.
    - logo (object): Logo pour l'affichage graphique.
    """
    
    def __init__(self,s,p,cl, em, e, r, color):
        self.symbole = s
        self.cell = p
        self.coding_level = cl
        self.energy_max = em
        self.energy = e
        self.richesse = r
        self.color = color
        self.rect = NULL
        self.logo = NULL
    
    
    def GetSymbol(self):
     
     """
    Renvoie le symbole du joueur.

    Returns:
    str: Symbole du joueur.
    """

     return self.symbole
    
    def GetPosition(self):
        """
        Renvoie la position actuelle du joueur sur la carte.

        Returns:
        tuple: Position actuelle du joueur.
        """
        return self.cell
    
    def GetCodingLevel(self):
       """
        Renvoie le niveau de codage du joueur.

        Returns:
        int: Niveau de codage du joueur.
        """
       return self.coding_level
    
    def GetEnergyMax(self):
       """
        Renvoie l'énergie maximale du joueur.

        Returns:
        int: Énergie maximale du joueur.
        """
       return self.energy_max
    
    def GetEnergy(self):
        """
        Renvoie l'énergie actuelle du joueur.

        Returns:
        int: Énergie actuelle du joueur.
        """
        return self.energy
    
    def GetMoneyAmount(self):
         """
        Renvoie le montant d'argent du joueur.

        Returns:
        int: Montant d'argent du joueur.
        """
         return self.richesse


    def ResetEnergy(self):
        """
        Réinitialise l'énergie du joueur à sa valeur maximale.

        Returns:
        None
        """
        self.energy = self.energy_max
        
    def ChangePosition(self,new_position):
       """
        Modifie la position du joueur.

        Args:
        - new_position (tuple): Nouvelle position du joueur sur la carte.

        Returns:
        None
        """
       self.cell = new_position

    def MovePosition(self,move):
       """
        Modifie la position du joueur en fonction d'un déplacement.

        Args:
        - move (tuple): Déplacement pour mettre à jour la position du joueur.

        Returns:
        None
        """
       self.cell = (self.cell[0] + move[0], self.cell[1] + move[1])

    def UpgradeCodingLevel(self):
        """
        Augmente le niveau de codage du joueur.

        Returns:
        None
        """
        if self.coding_level < 10:
           self.coding_level +=1
        else:
            print(" Vous etes deja au niveau max !")

    def UpgradeEnergyMax(self):
        """
        Augmente la limite d'énergie maximale du joueur.

        Returns:
        None
        """ 
        if self.energy_max < 10:
            self.energy_max += 1
        else:
            print(" Vous avez deja l'energie max !")
              
    
    def UpgradeEnergy(self, energy_amount):
        """
        Met à jour le niveau d'énergie du joueur en fonction d'un montant donné.

        Args:
        - energy_amount (int): Montant d'énergie à ajouter ou à retirer.

        Returns:
        None
        """
        if self.energy + energy_amount < 0:
             self.energy = 0 
             
        elif self.energy + energy_amount <= self.energy_max:
            self.energy += energy_amount
            
        elif self.energy + energy_amount >= self.energy_max:
            self.energy = energy_amount
            
        elif self.energy < 0:
            self.energy = 0




    
    def UpgradeMoneyAmount(self, money_amount):
        
        """
        Met à jour le montant d'argent du joueur en fonction d'un montant donné.

        Args:
        - money_amount (int): Montant d'argent à ajouter ou à retirer.

        Returns:
        None
        """
        if self.richesse + money_amount < 0:
            print("Vous ne possédez pas assez d'argent. Votre solde doit être supérieur à " + str(-money_amount) + " ฿ !")
        elif self.richesse < 5000:
            self.richesse += money_amount
        else:
            print("Vous avez atteint la limite de richesse !")

        
    def Draw(self, canvas, cellsize): # Uniquement utilisé pour la partie graphique 
        """
        Dessine le joueur sur un canvas pour la partie graphique.

        Args:
        - canvas: Zone graphique sur laquelle dessiner.
        - cellsize (int): Taille de la cellule pour le dessin.

        Returns:
        None
        """
        if self.rect != NULL:
            canvas.delete(self.rect)
           
        if self.logo != NULL:
            canvas.delete(self.logo)
                            
            
        self.rect = canvas.create_rectangle(
            self.cell[1] * cellsize,
            self.cell[0] * cellsize,
            (self.cell[1] + 1) * cellsize,
            (self.cell[0] + 1) * cellsize,
            fill=self.color
        )
       
        # Ajouter du texte au centre du coder
        x_center = (self.cell[1] * cellsize + (self.cell[1] + 1) * cellsize) / 2
        y_center = (self.cell[0] * cellsize + (self.cell[0] + 1) * cellsize) / 2

        self.logo = canvas.create_text(
            x_center,
            y_center,
            text=self.GetSymbol(),
            fill="white"  # Couleur du texte
        )    
    


        




