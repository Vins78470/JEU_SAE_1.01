from asyncio.windows_events import NULL
import time

class Coder():
    
    def __init__(self,s,p,cl, em, e, r, color):
        self.symbole = s
        self.position = p
        self.coding_level = cl
        self.energy_max = em
        self.energy = e
        self.richesse = r
        self.color = color
        self.rect = NULL
    
    def Draw(self, canvas, cellsize):
       if (self.rect != NULL):
            canvas.delete(self.rect)
            
       self.rect = canvas.create_rectangle(
           self.position[0] * cellsize,
           self.position[1] * cellsize,
           (self.position[0] + 1) * cellsize,
           (self.position[1] + 1) * cellsize,
            fill=self.color
        )
    
    
    def GetSymbol(self):
       return self.symbole
    
    def GetPosition(self):
       return self.position
    
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
       self.position = new_position

    def TranslatePosition(self,translation):
       self.position = (self.position[0] + translation[0], self.position[1] + translation[1])


    def UpgradeCodingLevel(self):
        if self.coding_level < 10:
           self.coding_level +=1
        else:
            print("Vous êtes deja au niveau max")

    def UpgradeEnergyMax(self):
         if self.energy_max < 10:
           self.energy_max += 1
         else:
            print("Vous avez deja l'energie max")
              
    
    def UpgradeEnergy(self,energy_amount):
         if self.energy < 0:
             self.energy = 0
             
         if self.energy - energy_amount <= self.energy_max :
             self.energy +=energy_amount
         else:
             self.energy = 0
    
    def UpgradeMoneyAmount(self, money_amount):
     print("oui")
     if self.richesse < 5000 and money_amount <=0 and (self.richesse - money_amount) >= 0: #Le coder perd de l'argent et on verifie si son argent sera tjrs >=0
            print("Jackpot1")
            self.richesse -= money_amount
     elif self.richesse < 5000 and money_amount >= 0 : #Le coder gagne de l'argent   
            print("Jackpot2")
            self.richesse += money_amount
           
     else:
        print("Vous ne possédez pas assez d'argent. Votre solde doit être supérieur à " + str(money_amount) + " ฿")
        

class Mission():
    
    def __init__(self,s, sw, rw,d,p):
        self.symbole = s
        self.starting_workload= sw
        self.remaining_workload = rw
        self.difficulty = d             
        self.position = p
        

    # Valeurs initiales pour que quand la mission réapparaisse elle reprenne ses attributs
        self.symbole_initial = s
        self.starting_workload_initial = sw
        self.remaining_workload_initial = rw
        self.difficulty_initial = d
        self.position_initial = p
        


    def GetSymbol(self):
        return self.symbole

    def GetPosition(self):
        return self.position

    def GetStartingWorkLoad(self):
        return self.starting_workload
    
    def GetRemainingWorkLoad(self):
        return self.remaining_workload
       
    
    def GetDifficulty(self):
        return self.difficulty



    def ResetValues(self):
        self.symbole = self.symbole_initial
        self.starting_workload = self.starting_workload_initial
        self.remaining_workload = self.remaining_workload_initial
        self.difficulty = self.difficulty_initial
        self.position = self.position_initial
       
    def UpgradeRemaningWorkLoad(self,amount):
        self.remaining_workload += amount
    
    def UpgradeRemainingWorkLoad(self,amount):
        if self.remaining_workload - amount >=0:
            self.remaining_workload += amount
        else:
            print("oe")
    
    def ResetRemainingWorkLoad(self):
        self.remaining_workload = 0


    
    


        




