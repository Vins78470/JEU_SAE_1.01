import random
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


def InitialisationCoder(Board,liste_coder,nb_coder):
   
    liste_symbole_coder = ['P1','P2','P3','P4']
    
    for i in range(nb_coder):
         liste_coder.append(Coder(liste_symbole_coder[i],(10,10),1,1,1,100,"blue"))
    
    return liste_coder


def CheckNombreCoder(nb_coder):
    if 1 <= nb_coder <= 4:
        return True
    else:
        print("Il faut choisir entre 1 et 4 coders")
        return False


def CheckDirectionInput(potential_position,coup_possible_coder):
    if potential_position in coup_possible_coder:
        return True
    else:
        print("Il faut choisir entre les touches h, b, g, d")
        return False
        



#Genere le nombre de missions qu'il y aura et créer des symboles pour ces missions
def GenerateSymbolMission(liste_symbole_missions):   
    
    nb_de_mission = random.randint(4,10)

    for j in range (1,nb_de_mission):
        liste_symbole_missions.append("M"+str(j))
   
    return liste_symbole_missions


# Prend en argument la géneration des symboles et par consequent son nombre de missions et créer des objets missions puis les mets dans une liste de mission

def InitialisationMission(liste_missions,liste_symbole_missions):

    for i in range(len(liste_symbole_missions)):

         random_i = random.randint(1,20)
         random_j = random.randint(1,20)

         liste_missions.append(Mission(liste_symbole_missions[i],2,2,2,(random_i,random_j)))
    
    return liste_missions


# Fonction pour vérifier si une position est dans la première ligne ou colonne
def est_dans_premiere_ligne_ou_colonne(position):
    x, y = position
    return x == 0 or y == 0


def CherchePosition(potential_position,coup_possible_coder):
   for cle, valeur in coup_possible_coder.items():
       if cle == potential_position:
            return valeur 



def IsCaseEmpty(position, liste_coder):
    for coder in liste_coder:
        if coder.GetPosition() == position:
            return False  # La case n'est pas vide, elle est occupée par un coder
    return True  # Aucun coder n'occupe cette case, elle est vide



def IsMovable(potential_position,coder,liste_coder):
  
    potential_next_position = (coder.GetPosition()[0] + potential_position[0], coder.GetPosition()[1] + potential_position[1])

    #Verification si il y a un autre coder deja sur la case potentiel
    if not IsCaseEmpty(potential_next_position, liste_coder):
        print("Case occupée, choisissez une autre case")
        return False  # La case n'est pas vide, le déplacement n'est pas possible
 
    # Vérification si la prochaine position est dans la première ligne ou colonne
    if est_dans_premiere_ligne_ou_colonne(potential_next_position):
        return False
    # Vérification si la prochaine position est dans les limites de la grille
    if 1 <= potential_next_position[0] <= 20 and 1 <= potential_next_position[1] <= 20:
        # Insérez ici d'autres conditions spécifiques à votre jeu si nécessaire
        return True  # La prochaine position est valide
    else:
        return False  # La prochaine position est en dehors des limites de la grille



def DrawPlayer(Board, potential_position, coder):
    new_position = (coder.GetPosition()[0] + potential_position[0], coder.GetPosition()[1] + potential_position[1])
    coder.ChangePosition(new_position)

    # Utilisation de nouvelles_positions[0] et nouvelles_positions[1] pour accéder aux indices x et y
    Board[new_position[0]][new_position[1]] = coder.GetSymbol()
    
def DeletePlayer(Board, coder):
    x, y = coder.GetPosition()
    symbol = coder.GetSymbol()

    # Remplacer le symbole du coder par une chaîne vide dans la case du tableau
    Board[x][y] = Board[x][y].replace(symbol, "  ")
    if Board[10][10] == "   ":
        Board[10][10] == "JC"


def DrawPlayerAtJobCenter(Board, liste_coder):
    symbols = ''
    for coder in liste_coder:
        symbols += coder.GetSymbol()  # Concatène les symboles des coders

    Board[10][10] = symbols  # Place les symboles concaténés dans la case [10][10] du plateau
    return Board 



def UpdateJobCenter(Board, liste_coder):
    center_position = (10, 10)  # Position du centre

    # Vérifie s'il y a un coder sur la case du centre
    for coder in liste_coder:
        if coder.GetPosition() == center_position:
            return  # Il y a un coder, donc on ne change pas la case

    # S'il n'y a aucun coder sur la case du centre, on la met à jour
    Board[center_position[0]][center_position[1]] = "JC"

# Dessine la mission sur la Board

def DrawMissions(Board,liste_missions):

    for mission in liste_missions:
        mission_pos = mission.GetPosition()
        Board[mission_pos[0]][mission_pos[1]] = mission.GetSymbol()
    
    return Board
        
# Quand le coder passe sur une mission, si elle n'est pas fini on la redessine 

def ReDrawMission(Board,liste_missions,coder):
    mission = FindMissionAssociatedToCoder(liste_missions,coder)
    x,y = mission.GetPosition()
    Board[x][y] = mission.GetSymbol()
    


# Affiche les infos des coders
def AfficherInfosCoder(liste_coder):
    coder_info_text = ""
    for i, coder in enumerate(liste_coder, 1):
        coder_info_text += f"Coder {i} :\n"
        coder_info_text += f"  - Symbole: {str(coder.GetSymbol())}\n"
        coder_info_text += f"  - Position: {str(coder.GetPosition())}\n"
        coder_info_text += f"  - Niveau de codage: {str(coder.GetCodingLevel())}\n"
        coder_info_text += f"  - Energie: {str(coder.GetEnergy())} / Energie maximale: {str(coder.GetEnergyMax())}\n"
        coder_info_text += f"  - Argent: {str(coder.GetMoneyAmount())} ฿\n\n"

    return coder_info_text



def CheckReapparitionMission(compt,mission_supprimé_a_check):

   return compt == mission_supprimé_a_check.GetDifficulty()*5


def DeleteMission(liste_missions, coder):
    mission = FindMissionAssociatedToCoder(liste_missions, coder)
    tmp_mission = mission
    liste_missions.remove(mission)
    return tmp_mission


# Cette partie du code s'exécuterait à chaque tour
def UpdateMissions(liste_missions,mission_supprimé_a_check):
    
    return liste_missions.append(mission_supprimé_a_check)

# Affiche les infos des missions

def AfficherInfosMissions(liste_missions):
    mission_info_text = ""
    for i, mission in enumerate(liste_missions, 1):
        mission_info_text += (
            f"  - Mission {i}: Symbole {mission.GetSymbol()}, "
            f"  - Position: {mission.GetPosition()}, "
            f"  - Travail de base a faire :  {mission.GetStartingWorkLoad()}, "
            f"  - Travail nécessaire: {mission.GetRemainingWorkLoad()}, "
            f"  - Difficulté: {mission.GetDifficulty()}\n"
        )      
    return mission_info_text




def IsCoderOnaMission(coder, list_missions):
    coder_position = coder.GetPosition()
    for mission in list_missions:
        mission_position = mission.GetPosition()
        if coder_position == mission_position:
            return True
    return False




""" Lorsqu'un coder, à la fin de son tour, dispose de 5000฿, alors le match se termine"""
def GameIsOver(coder):
    if coder.GetMoneyAmount(coder)==5000:
       print("Game Over")
       return True
    else:
       return False



def FindMissionAssociatedToCoder(liste_missions,coder):
    for mission in liste_missions:
        if coder.GetPosition() == mission.GetPosition():
            return mission
    print("pas de msision la ")



"""le coût en dollar est égal au carré du niveau désiré, fois 10\฿. Ces actions sont
possibles seulement si le coder dispose de l'argent nécessaire."""

def CoutDepenseArgentAuJobCenterPourEnergyMax(coder):
    if (coder.GetMoneyAmount() - ((coder.GetEnergyMax()+1)**2)*10) >= 0:
        coder.UpgradeMoneyAmount(-((coder.GetEnergyMax()+1)**2)*10)
        return True
    else:
        print("Vous n'avez pas assez d'argent pour augmenter votre energy max ") 
        return False



def CoutDepenseArgentAujobCenterPourCodingLevel(coder):
    if (coder.GetMoneyAmount() - ((coder.GetCodingLevel()+1)**2)*10) >= 0:
        return coder.UpgradeMoneyAmount(-((coder.GetCodingLevel()+1)**2)*10)
    else:
         print("Vous n'avez pas assez d'argent pour augmenter votre coding level")  

        
"""le coder perd un nombre de points d'energie égal à la difficulté de la mission"""

def DepenseCoderEnergyPourLaMission(coder,liste_missions):
    mission = FindMissionAssociatedToCoder(liste_missions,coder)
    return coder.UpgradeEnergy(-(mission.GetDifficulty()))
    


"""le RW de la mission diminue du CL du coder"""

def DepenseRwMission(coder,liste_missions):
    mission = FindMissionAssociatedToCoder(liste_missions,coder)
    return mission.UpgradeRemainingWorkLoad(-(coder.GetCodingLevel()))
    


    
"""Si en avançant une mission le coder amène la RW à 0 (ou moins), la mission est réalisée et le coder gagne un revenu égal au produit SW x D"""

def IsFinishMission(coder, liste_missions):
    mission = FindMissionAssociatedToCoder(liste_missions, coder)
    if mission.GetRemainingWorkLoad() == 0:
        return True



def MissionIsFinishedYouWinMoney(coder,liste_missions):
        mission = FindMissionAssociatedToCoder(liste_missions,coder)
        print("c winnn")
        return coder.UpgradeMoneyAmount(mission.GetStartingWorkLoad()*mission.GetDifficulty())



def EnoughEnergy(coder):
    if coder.GetEnergy() > 0:
        print("Tu peux faire la mission !")
        return True
    else:
        print("Pas assez d'énergie pour faire la mission retournez au job center !")




"""Si un coder se trouve sur le JC, il peut réaliser une des actions suivantes qui sont des upgrades :
augmenter de 1 son énergie max ;
ou bien augmenter de 1 son coding level."""

def CheckJobCenter(Board,coder):
    x,y = coder.GetPosition()
    if Board[10][10] == Board[x][y]:
        return True
    else:
        print(Board[10][10])


def AskChoiceAtJobCenter(coder):
    decisionLetter = input((" Augmentez son énergie max('a') ou augmenter votre coding level de 1 ('c') : "))
    return decisionLetter

def MakeChoiceAtJobCenter(coder, decisionLetter):
    
    if decisionLetter == 'a':
        if CoutDepenseArgentAuJobCenterPourEnergyMax(coder):
            return coder.UpgradeEnergyMax()
    elif decisionLetter == 'c':
        CoutDepenseArgentAujobCenterPourCodingLevel(coder)
        return coder.UpgradeCodingLevel()
    
    coder.ResetEnergy()


