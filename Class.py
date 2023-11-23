import time



class Coder():
    
    def __init__(self,s,p,cl, em, e, r):
        self.symbole = s
        self.position = p
        self.coding_level = cl
        self.energy_max = em
        self.energy = e
        self.richesse = r
    
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



    def UpgradeCodingLevel(self):
        if self.coding_level < 10:
           self.coding_level +=1
           
    def UpgradeEnergyMax(self):
         if self.energy_max < 10:
           self.coding_level +=1
    
    def UpgradeEnergy(self,energy_amount):
         if self.energy < 0:
             self.energy = 0
         if self.energy < self.energy_max:
             self.energy +=energy_amount
    
    def UpgradeMoneyAmount(self,money_amount):
         if self.richesse < 5000 and self.richesse -money_amount >= 0:
             self.richesse+= money_amount
        

class Mission():
    
    def __init__(self, sw, rw,d):
        self.starting_workload= sw
        self.remaining_worload = rw
        self.difficulty = d             


    def GetStartingWorkLoad(self):
        return self.starting_workload
    
    def GetRemainingWorkLoad(self):
        return self.remaining_workload
    
    def GetDifficulty(self):
        return self.difficulty


    def UpgradeStartingWorkLoad(self,amount):
        self.starting_workload -= amount 
    
    def UpgradeRemainingWorkLoad(self):
        self.remaining_workload = 0


    
    


        




