
from Rules import *
from Coder import *
from Mission import *
from PartieGraphique import *
from Game import *

# -*- coding: utf-8 -*-

#nb_coder = int(input(("A combien de coder(s) voulez vous jouer ? ")))
nb_coder = 1

mode = 0 #console
mode = 1 #window

game1 = Game(nb_coder, "facile")
game2 = Game(nb_coder, "intermediaire")
game3 = Game(nb_coder, "difficile")
#game.Configuration.ReadFromFile()

def Play(game, mode):
    game.start()
    if (mode == 0):
        game.play()
    elif (mode == 1): 
        windowForGame = WindowForGame(game, cell_size=50, nb_cell_width=21, nb_cell_height=21)
        windowForGame.draw()
        windowForGame.window.mainloop()
       

Play(game1, 0)