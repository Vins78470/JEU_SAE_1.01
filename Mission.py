﻿from asyncio.windows_events import NULL
import time


class Mission():
    
    def __init__(self,symbol, starting_workload, difficulty, position):
        self.symbol = symbol
        self.starting_workload= starting_workload
        self.remaining_workload = starting_workload
        self.difficulty = difficulty             
        self.position = position
        
    # Valeurs initiales pour que quand la mission réapparaisse elle reprenne ses attributs
        self.symbole_initial = symbol
        self.starting_workload_initial = starting_workload
        self.remaining_workload_initial = starting_workload
        self.difficulty_initial = difficulty
        self.position_initial = position

    def GetSymbol(self):
        return self.symbol

    def GetPosition(self):
        return self.position

    def GetStartingWorkLoad(self):
        return self.starting_workload
    
    def GetRemainingWorkLoad(self):
        return self.remaining_workload
       
    def GetDifficulty(self):
        return self.difficulty

    def ResetValues(self):
        self.symbol = self.symbole_initial
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


    
    


        




