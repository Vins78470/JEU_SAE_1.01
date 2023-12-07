from asyncio.windows_events import NULL
import time

class Coder():
    
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
       return self.symbole
    
    def GetPosition(self):
       return self.cell
    
    def GetCodingLevel(self):
       return self.coding_level
    
    def GetEnergyMax(self):
       return self.energy_max
    
    def GetEnergy(self):
        return self.energy
    
    def GetMoneyAmount(self):
        return self.richesse


    def ResetEnergy(self):
        self.energy = self.energy_max
        
    def ChangePosition(self,new_position):
       self.cell = new_position

    def MovePosition(self,move):
       self.cell = (self.cell[0] + move[0], self.cell[1] + move[1])

    def UpgradeCodingLevel(self):
        if self.coding_level < 10:
           self.coding_level +=1
        else:
            print(" Vous etes deja au niveau max !")

    def UpgradeEnergyMax(self):
         if self.energy_max < 10:
           self.energy_max += 1
         else:
            print(" Vous avez deja l'energie max !")
              
    
    def UpgradeEnergy(self, energy_amount):
        if self.energy + energy_amount < 0:
             self.energy = 0 
             
        elif self.energy + energy_amount <= self.energy_max:
            self.energy += energy_amount
            
        elif self.energy + energy_amount >= self.energy_max:
            self.energy = energy_amount
            
        elif self.energy < 0:
            self.energy = 0




    
    def UpgradeMoneyAmount(self, money_amount):
        if self.richesse + money_amount < 0:
            print("Vous ne possédez pas assez d'argent. Votre solde doit être supérieur à " + str(-money_amount) + " ฿ !")
        elif self.richesse < 5000:
            self.richesse += money_amount
        else:
            print("Vous avez atteint la limite de richesse !")

        
    def Draw(self, canvas, cellsize): # Uniquement utilisé pour la partie graphique 
           
           if self.rect != NULL:
                canvas.delete(self.rect)
           
           if self.logo != NULL:
                canvas.delete(self.rect)
                            
            
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
                text="P",
                fill="white"  # Couleur du texte
            )    
    


        




