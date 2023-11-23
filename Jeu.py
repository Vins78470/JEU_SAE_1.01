
from Class import *
import string

def InitBoard(Board):
    print("")
    print("------- Niveau 0 ------- : ")  
    print("")

    Board = [["  " for x in range(22)] for y in range(22)]     # Création d'une grille 21 par 21 remplie de chaine vide
    
    alphabet = list(string.ascii_uppercase[:21])  # Sélectionne les 21 premières lettres de l'alphabet
    
    for i in range(21):
        Board[0][i+1] = alphabet[i].ljust(2)  # Affiche les lettres de l'alphabet en lignes (i+1 a pour pas écraser les chiffres)
    for j in range(21):
        Board[j+1][0] = str(j).ljust(2) # Affiche les numéros en colonne (j+1 a pour pas écraser l'alphabet)
        
        
    Board[10][10] = "JC" #Initalise le job center
    return Board
 
def PrintBoard(Board):
    for i in range(len(Board)):
        print("\n" + "  " + " | ".join(Board[i]) + " | " + "\n")


def AffichageConsigne():
    pass


def GameIsOver(self):
    if Coder.GetMoneyAmount(self)==5000:
       return True
    else:
       return False



def CoutDepense(self):
    Coder.UpgradeMoneyAmount((Mission.GetDifficulty()**2)*10)
    pass


def FinishMission(self):
    if Mission.GetRemainingWorkLoad() == 0:
        Coder.UpgradeMoneyAmount(Mission.GetStartingWorkLoad()*Mission.GetDifficulty())
        
        