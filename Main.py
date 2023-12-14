# -*- coding: utf-8 -*-
from Rules import *
from Coder import *
from Mission import *
from PartieGraphique import *
from Game import *
# -*- coding: utf-8 -*-

 

mode = 0 #console
mode = 1 #window


nb_coder = int(input(("A combien de coder(s) voulez vous jouer ? ")))


# Verifie que l'utilisateur choisis entre 1 et 4 joueurs.

if CheckNombreCoder(nb_coder) == False:
    nb_coder = int(input(("A combien de coder(s) voulez vous jouer ? ")))
   

# Verifie que l'utilisateur choisis entre les 3 niveaux de difficultes.
difficultyChoice = input("Choisissez le niveau voulu (facile / intermediaire / difficile): ")

if CheckLevelChoice(difficultyChoice) == False:
    difficultyChoice = input("Choisissez le niveau voulu (facile / intermediaire / difficile): ")
    


if (difficultyChoice == "facile"):
    game = Game(nb_coder, difficultyChoice,nb_de_missions=random.randint(15,20))
    
elif (difficultyChoice == "intermediaire"):
    game = Game(nb_coder, difficultyChoice,nb_de_missions=random.randint(11,14))
    
elif (difficultyChoice == "difficile"):
    game = Game(nb_coder, difficultyChoice,nb_de_missions= random.randint(5,10))    

else: 
    print("Choisissez un niveau possible ! ")
   


def Play(game, mode):
    
    """
    G�re le déroulement du jeu en fonction du mode sp�cifi�.

    Arguments :
    game : Game
        L'instance du jeu a demarrer et et jouer.
    mode : int
        Le mode de jeu a executer (0 pour jouer dans la console, 1 pour jouer dans une fenetre graphique).

    Returns :
    None
        La fonction gere le demarrage et le deroulement du jeu selon le mode selectionne.
        Si le mode est 0, le jeu est joue dans la console.
        Si le mode est 1, le jeu est affiche dans une fenetre graphique.
    """    
        
    game.start()

    if (mode == 0): 
       game.play()
       
    windowForGame = NULL
    if (mode == 1): 
        windowForGame = WindowForGame(game, cell_size=30, nb_cell_width=22, nb_cell_height=22)
        windowForGame.play()
            
            


        



Play(game, 1) # Pour jouer en mode fenetre graphique (gardez bien la fenetre de la console ouverte pour avoir les messages d'intéraction !!!!).

#Play(game, 0) -> Pour jouer en mode console.