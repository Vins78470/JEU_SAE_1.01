import random

from Coder import *
from Mission import *
import string
# -*- coding: utf-8 -*-


def InitBoard(Board):

    """
    Initialise et retourne un plateau de jeu avec des coordonnées initiales.
    
    Args:
    - Board: tableau représentant le plateau de jeu
    
    Returns:
    - Board: plateau de jeu initialisé
    """

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

    """
    Affiche le plateau de jeu avec un alignement des symboles à droite.

    Args:
    - Board: tableau représentant le plateau de jeu
    """

    max_length = max(len(symbol) for row in Board for symbol in row)  # Longueur maximale des symboles
    for i in range(len(Board)):
        row = " | ".join(symbol.rjust(max_length) for symbol in Board[i])  # Alignement des symboles à droite
        print("\n" + "  " + row + " | " + "\n")



def CheckNombreCoder(nb_coder):
    """
    Vérifie si le nombre de "coders" est valide (entre 1 et 4).
    
    Args:
    - nb_coder: nombre de "coders" choisi
    
    Returns:
    - bool: True si le nombre est valide, False sinon
    """

    if 1 <= nb_coder <= 4:
        return True
    else:
        print(" Choisissez entre 1 a 4 coders ")
        return False


def CheckLevelChoice(difficultyChoice):
    
    """
    Vérifie si le choix de difficulté donné est valide.

    Args:
    - difficultyChoice: chaîne représentant le choix de difficulté

    Returns:
    - bool: True si la difficulté est valide, False sinon
    """

    valid_difficulties = ["facile", "intermediaire", "difficile"]
    return difficultyChoice in valid_difficulties



def CheckDirectionInput(potential_position,coup_possible_coder):

    """
    Vérifie si la position potentielle correspond à une direction valide pour le joueur.

    Args:
    - potential_position: tuple représentant la position potentielle
    - coup_possible_coder: dictionnaire des coups possibles pour le joueur

    Returns:
    - bool: True si la position potentielle est une direction valide, False sinon
    """

    if potential_position in coup_possible_coder:
        return True
    else:
        return False
    


def est_dans_premiere_ligne_ou_colonne(position):
    
    """
    Vérifie si une position donnée se situe sur la première ligne ou la première colonne d'une grille.

    Args:
    - position: tuple représentant les coordonnées (x, y) de la position

    Returns:
    - bool: True si la position est sur la première ligne ou colonne, False sinon
    """

    x, y = position
    return (x == 0 or y == 0)





def CherchePosition(potential_position,coup_possible_coder):
   
   """
    Cherche et retourne une valeur associée à une position dans un dictionnaire de coups possibles.

    Args:
    - potential_position: tuple représentant la position recherchée
    - coup_possible_coder: dictionnaire des coups possibles avec les positions comme clés

    Returns:
    - valeur: la valeur associée à la position recherchée, si elle existe, sinon None
    """
   
   for cle, valeur in coup_possible_coder.items():
       if cle == potential_position:
            return valeur 


def IsCaseEmpty(position, liste_coder):

    """
    Vérifie si une case spécifique sur le plateau de jeu est vide.

    Args:
    - position: tuple représentant les coordonnées de la case à vérifier
    - liste_coder: liste des objets "coder" actuellement sur le plateau

    Returns:
    - bool: True si la case est vide, False si elle est occupée par un "coder"
    """
    
    for coder in liste_coder:
        if position == (10,10):
            return True
        if (coder.GetPosition() == position):
            return False  # La case n'est pas vide, elle est occupée par un coder
    return True  # Aucun coder n'occupe cette case, elle est vide



def IsMovable(potential_position,coder,liste_coder):
    
    """
    Vérifie si un "coder" peut se déplacer vers une position potentielle sur la grille du jeu.

    Args:
    - potential_position: tuple représentant la position potentielle de déplacement
    - coder: objet "coder" pour lequel le déplacement est vérifié
    - liste_coder: liste des "coders" actuellement sur le plateau

    Returns:
    - bool: True si le déplacement est possible, False sinon
    """
  
    potential_next_position = (coder.GetPosition()[0] + potential_position[0], coder.GetPosition()[1] + potential_position[1])

    #Verification si il y a un autre coder deja sur la case potentiel
    if not IsCaseEmpty(potential_next_position, liste_coder):
        print("Case occupée, choisissez une autre case !")
        print("\n")
        return False  # La case n'est pas vide, le déplacement n'est pas possible
 
    # Vérification si la prochaine position est dans la première ligne ou colonne
    if est_dans_premiere_ligne_ou_colonne(potential_next_position):
        return False
    # Vérification si la prochaine position est dans les limites de la grille
    if 1 <= potential_next_position[0] <= 21 and 1 <= potential_next_position[1] <= 21:
        # Insérez ici d'autres conditions spécifiques à votre jeu si nécessaire
        return True  # La prochaine position est valide
    else:
        return False  # La prochaine position est en dehors des limites de la grille


def DrawPlayer(Board, coder):

    """
    Met à jour le plateau de jeu en plaçant le symbole représentant un "coder" à une position spécifique.

    Args:
    - Board: tableau représentant le plateau de jeu
    - coder: objet "coder" à placer sur le plateau

    Modifie:
    - Board: met à jour le plateau en plaçant le symbole du "coder" à sa position actuelle
    """

    # Utilisation de nouvelles_positions[0] et nouvelles_positions[1] pour accéder aux indices x et y

    Board[coder.cell[0]][coder.cell[1]] = coder.GetSymbol()

    
def DeletePlayer(Board, coder):

    """
    Supprime un 'coder' du plateau de jeu en remplaçant son symbole par une chaîne vide à sa position spécifique.
    Met également à jour le statut du Job Center sur le plateau.

    Args:
    - Board: tableau représentant le plateau de jeu
    - coder: objet 'coder' à supprimer du plateau

    Modifie:
    - Board: met à jour le plateau en supprimant le symbole du 'coder' à sa position actuelle
    """

    x, y = coder.GetPosition()
    symbol = coder.GetSymbol()

    # Remplacer le symbole du coder par une chaîne vide dans la case du tableau
    Board[x][y] = Board[x][y].replace(symbol, "  ")
    if Board[10][10] == "   ":
        Board[10][10] == "JC"


def DrawPlayerAtJobCenter(Board, liste_coder):

    """
    Met à jour le plateau de jeu en plaçant les symboles concaténés de tous les 'coders' à la position du Job Center.

    Args:
    - Board: tableau représentant le plateau de jeu
    - liste_coder: liste des objets 'coder' présents sur le plateau

    Returns:
    - Board: plateau de jeu mis à jour avec les symboles des 'coders' au Job Center
    """

    symbols = ''
    for coder in liste_coder:
        symbols += coder.GetSymbol()  # Concatène les symboles des coders

    Board[10][10] = symbols  # Place les symboles concaténés dans la case [10][10] du plateau
    return Board 



def UpdateJobCenter(Board, liste_coder):

    """
    Met à jour l'état du Job Center sur le plateau de jeu en fonction de la présence d'un 'coder' à une position spécifique.

    Args:
    - Board: tableau représentant le plateau de jeu
    - liste_coder: liste des objets 'coder' présents sur le plateau

    Modifie:
    - Board: met à jour la case du Job Center si aucun 'coder' n'est présent à sa position
    """
    
    center_position = (10, 10)  # Position du centre

    # Vérifie s'il y a un coder sur la case du centre
    for coder in liste_coder:
        if coder.GetPosition() == center_position:
            return  # Il y a un coder, donc on ne change pas la case

    # S'il n'y a aucun coder sur la case du centre, on la met à jour
    Board[center_position[0]][center_position[1]] = "JC"

# Dessine la mission sur la Board

def DrawMissions(Board,liste_missions):
    
    """
    Met à jour le tableau `Board` avec les symboles des missions à leurs positions respectives.

    Args:
    - Board (list): Le tableau représentant le plateau de jeu.
    - liste_missions (list): La liste des objets de mission à placer sur le plateau.

    Returns:
    - list: Le tableau `Board` mis à jour avec les symboles des missions aux positions correspondantes.
    """

    for mission in liste_missions:
        DrawMission(Board, mission)

    return Board
        



# Quand le coder passe sur une mission, si elle n'est pas fini on la redessine 

def DrawMission(Board, mission):
    """
    Redessine la mission associée au codeur sur le plateau s'il n'a pas encore été terminé.

    Args:
    - Board (list): Le tableau représentant le plateau de jeu.
    - liste_missions (list): La liste des objets de mission présents sur le plateau.
    - coder (Coder): L'objet représentant le codeur associé à une mission.

    Returns:
    - None
    """
    if mission.est_disponible():
        x,y = mission.GetPosition()
        Board[x][y] = mission.GetSymbol()
    

    
    


# Affiche les infos des coders

def AfficherInfosCoder(liste_coder):
    
    """
    Affiche les informations détaillées de chaque codeur de la liste.

    Args:
    - liste_coder (list): Liste des objets représentant les codeurs.

    Returns:
    - str: Texte contenant les informations détaillées de chaque codeur.
    """
    coder_info_text = ""
    for i, coder in enumerate(liste_coder, 1):
        coder_info_text += f"Coder {i} :\n"
        coder_info_text += f"  - Symbole: {str(coder.GetSymbol())}\n"
        coder_info_text += f"  - Position: {str(coder.GetPosition())}\n"
        coder_info_text += f"  - Niveau de codage: {str(coder.GetCodingLevel())}\n"
        coder_info_text += f"  - Energie: {str(coder.GetEnergy())} / Energie maximale: {str(coder.GetEnergyMax())}\n"
        coder_info_text += f"  - Argent: {str(coder.GetMoneyAmount())} ฿\n\n"

    return coder_info_text





def DeleteMission(liste_missions, coder):
    """
    Supprime la mission associée à un codeur de la liste des missions.

    Args:
    - liste_missions (list): Liste des missions à gérer.
    - coder (object): Codeur dont la mission associée doit être supprimée.

    Returns:
    - object: La mission supprimée de la liste.
    """    

    mission = GetMissionOnPosition(liste_missions, coder.GetPosition())
    tmp_mission = mission
    liste_missions.remove(mission)
    return tmp_mission



# Affiche les infos des missions

def AfficherInfosMissions(liste_missions):
    
    """
    Affiche les informations sur les missions de la liste.

    Args:
    - liste_missions (list): Liste des missions à afficher.

    Returns:
    - str: Texte contenant les détails des missions présentes dans la liste.
    """
    mission_info_text = ""
    for i, mission in enumerate(liste_missions, 1):
        if i < 10:
            mission_info_text += (
                    f"  - Mission  0{i}              : Symbole {mission.GetSymbol()}, ")
        else:
            mission_info_text += (
                    f"  - Mission  {i}              : Symbole {mission.GetSymbol()}, ")

        mission_info_text += (
            f"  - Position                  : {mission.GetPosition()}, "
            f"  - Travail de base a faire   : {mission.GetStartingWorkLoad()}, "
            f"  - Travail nécessaire        : {mission.GetRemainingWorkLoad()}, "
            f"  - Difficulté                : {mission.GetDifficulty()}"
            f"  - Indisponible pdt nb tours : {mission.unavailable_for_nb_round}\n"
        )      
    return mission_info_text


def IsPositionOnMission(list_missions, position):
    
    """
    Vérifie si un coder est actuellement sur une mission.

    Args:
    - coder (Coder): Le coder dont la position doit être vérifiée.
    - list_missions (list): La liste des missions à vérifier.

    Returns:
    - bool: True si le coder est sur une mission, False sinon.
    """
    for mission in list_missions:
        if position == mission.GetPosition():
            return True
    return False


def IsGameOver(coder):
    """
    Vérifie si le match est terminé en fonction de la quantité d'argent accumulée par le coder.

    Args:
    - coder (Coder): Le coder à évaluer pour savoir si le match est terminé.

    Returns:
    - bool: True si le montant d'argent du coder atteint ou dépasse 5000฿, sinon False.
    """
    if coder.GetMoneyAmount() >= 5000 or coder.round == 1000:
        return True
    else:
        return False

def GetMissionOnPosition(liste_missions, position):
    """
    Trouve la mission associée à une position .

    Args:
    - liste_missions (list): Liste des missions existantes.
    - position: positio sous forme de tuple.

    Returns:
    - Mission: La mission associée au coder s'ils partagent la même position, sinon None.
    """    
    
    for mission in liste_missions:
        if position == mission.GetPosition():
            return mission
    return None


"""le coût en dollar est égal au carré du niveau désiré, fois 10\฿. Ces actions sont
possibles seulement si le coder dispose de l'argent nécessaire."""

def CoutDepenseArgentAuJobCenterPourEnergyMax(coder):
    
    """
    Calcule le coût en dollar pour augmenter l'énergie maximale du coder au Job Center.

    Args:
    - coder (Coder): Le coder pour lequel on veut augmenter l'énergie maximale.

    Returns:
    - bool: True si le coder a assez d'argent pour augmenter son énergie maximale, False sinon.
    """
    
    if (coder.GetMoneyAmount() - ((coder.GetEnergyMax()+1)**2)*10) >= 0:
        coder.UpgradeMoneyAmount(-((coder.GetEnergyMax()+1)**2)*10)
        return True
    else:
        print(" Vous n'avez pas assez d'argent pour augmenter votre energie max. ") 
        print("\n")
        return False



def CoutDepenseArgentAujobCenterPourCodingLevel(coder):
    
    """
    Calcule le coût en dollars pour augmenter le niveau de codage du coder au Job Center.

    Args:
    - coder (Coder): Le coder pour lequel on veut augmenter le niveau de codage.

    Returns:
    - bool ou None: Si le coder a assez d'argent pour augmenter son niveau de codage,
      cela met à jour le niveau de codage et retourne True. Sinon, affiche un message
      et retourne None.
    """
    cost = ((coder.GetCodingLevel() + 1) ** 2) * 10
    if (coder.GetMoneyAmount() - cost) >= 0:
        coder.UpgradeMoneyAmount(-cost)
        return coder.UpgradeCodingLevel()
    else:
        print(" Vous n'avez pas assez d'argent pour augmenter votre coding level. ")
        print("\n")
        return None

        
"""le coder perd un nombre de points d'energie égal à la difficulté de la mission"""

def DepenseCoderEnergyPourLaMission(coder,liste_missions):
    
    """
    Réduit l'énergie du coder en fonction de la difficulté de la mission.

    Args:
    - coder (Coder): Le coder effectuant la mission.
    - liste_missions (list[Mission]): La liste des missions disponibles.

    Returns:
    - int: La nouvelle valeur de l'énergie du coder après la dépense pour la mission.
    """
    
    mission = GetMissionOnPosition(liste_missions,coder.GetPosition())
    return coder.UpgradeEnergy(-(mission.GetDifficulty()))
    


"""le RW de la mission diminue du CL du coder"""

def DepenseRwMission(coder,liste_missions):
    
    """
    Réduit la charge de travail restante d'une mission en fonction du niveau de codage du coder.

    Args:
    - coder (Coder): Le coder effectuant la mission.
    - liste_missions (list[Mission]): La liste des missions disponibles.

    Returns:
    - int: La nouvelle valeur de la charge de travail restante de la mission après la dépense par le coder.
    """
    mission = GetMissionOnPosition(liste_missions,coder.GetPosition())
    return mission.UpgradeRemainingWorkLoad(-(coder.GetCodingLevel()))
    


    
"""Si en avançant une mission le coder amène la RW à 0 (ou moins), la mission est réalisée et le coder gagne un revenu égal au produit SW x D"""

def IsFinishMission(coder, liste_missions):
    
    """
    Vérifie si une mission est terminée par un coder et réinitialise ses valeurs si elle est accomplie.

    Args:
    - coder (Coder): Le coder qui effectue la mission.
    - liste_missions (list[Mission]): La liste des missions disponibles.

    Returns:
    - bool: True si la mission est terminée et réinitialisée, False sinon.
    """
    
    mission = GetMissionOnPosition(liste_missions, coder.GetPosition())
    if mission.GetRemainingWorkLoad() == 0:
       mission.ResetValues()
       return True



def MissionIsFinishedYouWinMoney(coder,liste_missions):
    """
    Donne de l'argent au coder une fois la mission terminée.

    Args:
    - coder (Coder): Le coder ayant terminé la mission.
    - liste_missions (list[Mission]): La liste des missions disponibles.

    Returns:
    - float: Le montant d'argent gagné par le coder en fonction de la mission accomplie.
    """    
    mission = GetMissionOnPosition(liste_missions,coder.GetPosition())
    return coder.UpgradeMoneyAmount(mission.GetStartingWorkLoad()*mission.GetDifficulty())



def EnoughEnergy(coder):
    """
    Vérifie si le coder a suffisamment d'énergie pour effectuer une mission.

    Args:
    - coder (Coder): Le coder à vérifier.

    Returns:
    - bool: True si le coder a suffisamment d'énergie, False sinon.
    """
    
    if coder.GetEnergy() > 0:
        return True
    else:
        print(" Vous n'avez pas assez d'énergie pour faire la mission retournez au job center ! ")
        print("\n")



def IsJobCenter(Board, position):
    
    """
    Vérifie si un coder se trouve sur le Job Center pour effectuer des améliorations : 
    augmenter de 1 son énergie maximale ou son niveau de codage.

    Args:
    - Board (list): Le plateau de jeu.
    - coder (Coder): Le coder à vérifier.

    Returns:
    - bool: True si le coder se trouve sur le Job Center, False sinon.
    """
    
    x,y = position
    if Board[10][10] == Board[x][y]:
        return True
    else:
        return False


def AskChoiceAtJobCenter():
    
    """
    Propose au joueur de choisir entre deux actions possibles au Job Center :
    - Augmenter l'énergie maximale ('a')/ Via un bouton pour la partie graphique.
    - Augmenter le niveau de codage de 1 ('c')/ Via un des bouton pour la partie graphique.
    Le joueur peut également choisir de ne rien faire en sélectionnant une direction.

    Returns:
    - str: La lettre correspondant à l'action choisie.
    """
    
    print("\n")
    decisionLetter = input(" Augmentez son énergie max('a') ou augmenter votre coding level de 1 ('c') ou ne faites rien (choisir une direction): ")
    print("\n")
    print("\n")
    return decisionLetter




def MakeChoiceAtJobCenter(coder, decisionLetter):
    
    """
    Effectue un choix au Job Center en fonction de la lettre de décision reçue.

    Arguments :
    coder : Coder
        L'instance du Coder effectuant le choix.
    decisionLetter : str
        Lettre représentant le choix du joueur ('a' pour augmenter l'énergie max, 'c' pour augmenter le niveau de codage).

    Returns :
    bool or None
        Si l'opération est réussie (l'énergie max ou le niveau de codage est augmenté), retourne True, sinon False.
        Si aucune action n'est réalisée, retourne None.
    """
    
    coder.ResetEnergy() # On reset l'energie dans tout les cas

    if decisionLetter == 'a':
        if CoutDepenseArgentAuJobCenterPourEnergyMax(coder):
            coder.UpgradeEnergyMax()

    elif decisionLetter == 'c':
        CoutDepenseArgentAujobCenterPourCodingLevel(coder)
        return coder.UpgradeCodingLevel()



