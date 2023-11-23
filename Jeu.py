
import code
import symbol
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


def InitialisationJoueur(Board,liste_coder,nb_joueur):
    liste_symbole = ['P1','P2','P3','P4']
    
    for i in range(nb_joueur):
         liste_coder.append(Coder(liste_symbole[i],Board[10][10],10,1,1,0))
    
    return liste_coder


def DrawPlayer(Board, liste_coder):
    symbols = ''
    for coder in liste_coder:
        symbols += coder.GetSymbol()  # Concatène les symboles des joueurs

    Board[10][10] = symbols  # Place les symboles concaténés dans la case [10][10] du plateau
    return Board     
        

def AfficherInfosJoueur(liste_coder):
    for i, coder in enumerate(liste_coder,1): # Affiche les infos des joueurs de 1 a nb_de_joueur 
        print("Le joueur " + str(i) +" a le symbole "+ coder.GetSymbol())
        print("Le joueur " + str(i) +" a comme coding level "+ str(coder.GetCodingLevel()))
        print("Le joueur " + str(i) +" a comme energie "+ str(coder.GetEnergy()))
        print("Le joueur " + str(i) +" a "+ str(coder.GetMoneyAmount()) + " ฿ ")
        print("\n")


""" Lorsqu'un coder, à la fin de son tour, dispose de 5000฿, alors le match se termine"""
def GameIsOver(self):
    if Coder.GetMoneyAmount(self)==5000:
       print("Game Over")
       return True
    else:
       return False


"""le coût en dollar est égal au carré du niveau désiré, fois 10\฿. Ces actions sont
possibles seulement si le coder dispose de l'argent nécessaire."""

def CoutDepense(self):
    Coder.UpgradeMoneyAmount((Mission.GetDifficulty()**2)*10)

        
"""le coder perd un nombre de points d'energie égal à la difficulté de la mission"""
def CoutJoueurEnMission(self):
    Coder.UpgradeEnergy(-(Mission.GetDifficulty()))
    
"""le RW de la mission diminue du CL du coder"""
def DepenseEnergyMission():
    Mission.UpgradeRemainingWorkLoad(Coder.GetCodingLevel())
    


    
"""Si en avançant une mission le coder amène la RW à 0 (ou moins), la mission est réalisée et le coder gagne un revenu égal au produit SW x D"""

def IsFinishMission(self): 
   if Mission.GetRemainingWorkLoad() == 0:
       Coder.UpgradeMoneyAmount(Mission.GetStartingWorkLoad()*Mission.GetDifficulty())


"""Si un coder se trouve sur le JC, il peut réaliser une des actions suivantes qui sont des upgrades :
augmenter de 1 son énergie max ;
ou bien augmenter de 1 son coding level."""

def CheckJobCenter(Board,self):
    if Board[10][10] == Coder.GetPosition():
        requete_job_center = input(("Augmentez son énergie(A) ou augmenter votre coding level de 1 (l)"))
        if requete_job_center == 'a':
            Coder.UpgradeEnergy(1)
        elif requete_job_center == 'l':
            Coder.UpgradeCodingLevel(1)
    
        