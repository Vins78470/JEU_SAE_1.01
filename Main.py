
from Rules import *
from Coder import *
from Mission import *
from PartieGraphique import *
from Game import *

# -*- coding: utf-8 -*-

mode = 0 #console
mode = 1 #window


nb_coder = int(input(("A combien de coder(s) voulez vous jouer ? ")))

difficultyChoice = input("Choisissez le niveau voulu (facile / intermediaire / difficile): ")

if (difficultyChoice == "facile"):
    game = Game(nb_coder, difficultyChoice,nb_de_missions=random.randint(15,20))
    
elif (difficultyChoice == "intermediaire"):
    game = Game(nb_coder, difficultyChoice,nb_de_missions=random.randint(11,14))
    
elif (difficultyChoice == "difficile"):
    game = Game(nb_coder, difficultyChoice,nb_de_missions= random.randint(5,10))    

else: 
   print("Choisissez un niveau possible ! ")
   




#game2 = Game(nb_coder, "intermediaire")
#game3 = Game(nb_coder, "difficile")
#game.Configuration.ReadFromFile()

def Play(game, mode):
    game.start()
    if (mode == 0):
        game.play()
    elif (mode == 1): 
        windowForGame = WindowForGame(game, cell_size=50, nb_cell_width=21, nb_cell_height=21)
        windowForGame.draw()
        windowForGame.window.mainloop()
       

Play(game, 0)