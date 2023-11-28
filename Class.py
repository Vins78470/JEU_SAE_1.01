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





    def ResetEnergy(self):
        self.energy = self.energy
        
    def ChangePosition(self,new_position):
       self.position = new_position


    def UpgradeCodingLevel(self):
        if self.coding_level < 10:
           self.coding_level +=1
           
    def UpgradeEnergyMax(self):
         if self.energy_max < 10:
           self.energy_max += 1
    
    def UpgradeEnergy(self,energy_amount):
         if self.energy < 0:
             self.energy = 0
             
         if self.energy <= self.energy_max and self.energy - energy_amount >= 0:
             self.energy -=energy_amount
         else:
             self.energy = 0
    
    def UpgradeMoneyAmount(self, money_amount):
     print("oui")
     if self.richesse < 5000 and (self.richesse - money_amount) >= 0:
            print("Jackpot")
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



    def ChangeMission():
        pass
    
    def UpgradeRemaningWorkLoad(self,amount):
        self.remaining_workload += amount
    
    def UpgradeRemainingWorkLoad(self,amount):
        if self.remaining_workload - amount >=0:
            self.starting_workload += amount
        else:
            print("oe")
    
    def ResetRemainingWorkLoad(self):
        self.remaining_workload = 0


    
    


        




