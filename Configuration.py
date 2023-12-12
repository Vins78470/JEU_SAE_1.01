import json
import random
# -*- coding: utf-8 -*-


class Configuration:
    
    def __init__(self, level):
       
        self.starting_workload = 1
        self.difficulty = 1
        self.level = level
        self.json_file = f'{level}_missions.json'
        self.liste_data_mission = []

        self.UpdateFile()
        self.ReadFromFile() # On lit les donn�es qui viennent d'�tre �crites dans le fichier json.
        
    def UpdateFile(self):
        if self.level == "facile":
            self.starting_workload = random.randint(1, 3)
            self.difficulty = random.randint(1, 3)
         
            
        elif self.level == "intermediaire":
            self.starting_workload = random.randint(4, 8)
            self.difficulty = random.randint(4, 8)
          
            
        elif self.level == "difficile":
            self.starting_workload = random.randint(9, 12)
            self.difficulty = random.randint(8, 12)
          
        
        self.WriteToFile() # Ecriture des fichiers en fonction du choix de niveau
        
    def WriteToFile(self):
        mission_data = {
            "starting_workload": self.starting_workload,
            "difficulty": self.difficulty
        }
        
        with open(self.json_file, 'w') as file:
            json.dump(mission_data, file, indent=4)
            
    def ReadFromFile(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                self.starting_workload = data["starting_workload"]
                self.difficulty = data["difficulty"]
        except FileNotFoundError:
            pass 
