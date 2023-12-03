import json
import random

def generate_missions(num_missions, level):
    missions = []
    for i in range(num_missions):
        if level == "facile":
            starting_workload = random.randint(1, 5)
            difficulty = random.randint(1, 3)
        elif level == "intermédiaire":
            starting_workload = random.randint(4, 8)
            difficulty = random.randint(2, 5)
        elif level == "difficile":
            starting_workload = random.randint(7, 10)
            difficulty = random.randint(4, 7)
        
        mission_data = {
            "starting_workload": starting_workload,
            "difficulty": difficulty
        }
        missions.append(mission_data)
    return missions

# Générer une liste de missions pour chaque niveau de difficulté avec 10 éléments
facile_missions = generate_missions(10, "facile")
intermediaire_missions = generate_missions(10, "intermédiaire")
difficile_missions = generate_missions(10, "difficile")

# Enregistrer les listes de missions dans des fichiers JSON distincts
with open('facile_missions.json', 'w') as facile_file:
    json.dump(facile_missions, facile_file, indent=4)

with open('intermediaire_missions.json', 'w') as intermediaire_file:
    json.dump(intermediaire_missions, intermediaire_file, indent=4)

with open('difficile_missions.json', 'w') as difficile_file:
    json.dump(difficile_missions, difficile_file, indent=4)
