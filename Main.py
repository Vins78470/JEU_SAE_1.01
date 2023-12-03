
from Rules import *
from Class import *
from PartieGraphique import *
from Game import *

# -*- coding: utf-8 -*-



nb_coder = int(input(("A combien de coder(s) voulez vous jouer ? ")))


windowAndGame = WindowAndGame(cell_size=50, nb_cell_width=21, nb_cell_height=21)
windowAndGame.game.start(nb_coder)

windowAndGame.game.play()
windowAndGame.draw()
      
windowAndGame.window.mainloop()