import json
import random


class Configuration:

    def __init__(self, level):

        self.starting_workload = 1
        self.difficulty = 1

        if level == "facile":
            starting_workload = random.randint(1, 5)
            difficulty = random.randint(1, 3)
            self.WriteToFile('facile_missions.json');
        elif level == "intermediaire":
            starting_workload = random.randint(4, 8)
            difficulty = random.randint(4, 5)
            self.WriteToFile('intermediaire_missions.json');
        elif level == "difficile":
            starting_workload = random.randint(7, 10)
            difficulty = random.randint(6, 7)
            self.WriteToFile('difficile_missions.json');
        
        mission_data = {
            "starting_workload": starting_workload,
            "difficulty": difficulty
        }

            
    def ReadFromFile(self, jsonfile):            

        # Enregistrer les listes de missions dans des fichiers JSON distincts
        with open(jsonfile, 'r') as file:
            json.dump(self, file, indent=4)
        

    def WriteToFile(self, jsonfile):            

        # Enregistrer les listes de missions dans des fichiers JSON distincts
        #with open(jsonfile, 'w') as file:
        #    json.dump(self, file, indent=4)
        pass