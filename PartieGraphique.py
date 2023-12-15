
from tkinter import *
from Coder import *
from Mission import *
from Rules import AfficherInfosCoder, AfficherInfosMissions
from Game import *
# coding: utf-8



class WindowForGame:

    
    def __init__(self, game, cell_size, nb_cell_width, nb_cell_height):
      
        self.CELL_SIZE = cell_size
        self.NB_CELL_WIDTH = nb_cell_width
        self.NB_CELL_HEIGHT = nb_cell_height
        self.WIDTH = self.CELL_SIZE * self.NB_CELL_WIDTH
        self.HEIGHT = self.CELL_SIZE * self.NB_CELL_HEIGHT
        self.LEN = self.WIDTH  * self.HEIGHT
        self.game = game
        self.round = 0
        self.window = Tk()
        self.window.title("ESN GAME")

        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()


        self.draw_board()  # Appel de la methode draw_board() pour dessiner la grille d�s la creation de la fenetre
        
        self.canvas.bind_all('<KeyPress>', self.move_coder_on_key_pressed)

        self.missions_label = Label(self.window, text="")
        self.coder_label = Label(self.window, text="")
        
        # Place le texte "JC" au milieu de la position (10, 10)
        self.canvas.create_text(10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                text="JC",
                                font=("Arial", 20),  
                                fill="black")  # Couleur du texte (ici noir)

        
        self.btn_passer_tour = Button(self.window, text="Passer son tour", command=self.passer_tour)
        self.btn_passer_tour.pack(padx=20, pady=10)

    def passer_tour(self):
        self.round += 1  # Incrémenter le tour actuel

       
        

        
        
        
    def draw_info_missions(self):
        # Cr�ation de la cha�ne de texte pour les informations sur les missions
        mission_info_text = "Liste des missions :\n"
        mission_info_text = AfficherInfosMissions(self.game.liste_missions)

        self.missions_label.destroy()
        self.missions_label = Label(self.window, text=mission_info_text)
        # Cr�ation du label avec les informations des missions
        #mission_info_label = Label(self.window, text=mission_info_text)
        self.missions_label.pack(side="right",anchor="n", padx=10, pady=10)
        


        
    def draw_infos_coder(self):
        # Creation de la chaine de texte pour les informations sur le coder
        mission_info_text = "Infos coder(s) :\n"
        mission_info_text = AfficherInfosCoder(self.game.liste_coder)

        self.coder_label.destroy()
        self.coder_label = Label(self.window, text=mission_info_text)
        
        # Cr�ation du label avec les informations des missions
        self.coder_label.pack(side="left",anchor="n", fill='y', padx=10, pady=10)

    
    def draw_board(self):
        alphabet = list(string.ascii_uppercase[:22])
        for i in range(self.NB_CELL_HEIGHT ):
            for j in range(self.NB_CELL_WIDTH ):
                x1 = i * self.CELL_SIZE
                y1 = j * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
                if j == 0 and i > 0:
                    self.canvas.create_text(i * self.CELL_SIZE + self.CELL_SIZE // 2,
                             j * self.CELL_SIZE + self.CELL_SIZE // 2,
                             text=alphabet[i-1],
                             font=("Arial", 20),
                             fill="black")
                if i == 0 and j > 0:
                    self.canvas.create_text(i * self.CELL_SIZE + self.CELL_SIZE // 2,
                            j * self.CELL_SIZE + self.CELL_SIZE // 2,
                            text=j,
                            font=("Arial", 20),
                            fill="black")

                
   


    def draw_missions(self):
        
        for mission in self.game.liste_missions:
             
            mission_x, mission_y = mission.GetPosition()  # Obtient la position de la mission dans la grille
            mission_number = mission.GetSymbol()  # Récupère le numéro de la mission
               
            # dans une l'interface graphique, les axes sont inversés, ce qui signifie que les coordonnées y de la grille deviennent les coordonnées x dans l'interface graphique, et vice versa.
            mission_x_graphic = mission_y * self.CELL_SIZE
            mission_y_graphic = mission_x * self.CELL_SIZE
                
            # Dessin de la mission
            x1 = mission_x_graphic
            y1 = mission_y_graphic
            x2 = mission_x_graphic + self.CELL_SIZE
            y2 = mission_y_graphic + self.CELL_SIZE
            
            fillcolor = 'yellow' 
            if (mission.est_disponible() == False):
                fillcolor = 'red'
                
            self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill=fillcolor)
            self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=f"{mission_number}", fill='black')

    def ameliorer_energie_max(self,coder):

        if CoutDepenseArgentAuJobCenterPourEnergyMax(coder):
            coder.UpgradeEnergyMax()
            print("Bien Améliorer l'énergie maximale")

    def ameliorer_niveau_codage(self,coder):

         if CoutDepenseArgentAujobCenterPourCodingLevel(coder):
            coder.UpgradeCodingLevel()
            print("Bien Améliorer le niveau de codage")
           
    
    def move_coder_on_key_pressed(self, event):
        
        keyPressed = event.keysym
        moveDirection = (0, 0)
        current_coder_index = (self.round + 1) % self.game.nb_coder
        coder = self.game.liste_coder[current_coder_index]
        
        if current_coder_index == len(self.game.liste_coder)-1:
            if IsGameOver(coder):
                self.display_end()
                return
        
        if keyPressed == "Up":
            moveDirection = (-1, 0)
        elif keyPressed == "Down":
            moveDirection = (1, 0)
        elif keyPressed == "Left":
            moveDirection = (0, -1)
        elif keyPressed == "Right":
            moveDirection = (0, 1)
    
        if moveDirection != (0, 0):
            self.game.playOneRound(coder, moveDirection, self.round)
            self.round += 1
        
        if hasattr(self, "btn_energie_max"):
            self.btn_energie_max.destroy()  # Supprime le bouton s'il existe déjà
        if hasattr(self, "btn_niveau_codage"):
            self.btn_niveau_codage.destroy()  # Supprime le bouton s'il existe déjà


        if IsJobCenter(self.game.Board, coder.GetPosition()):

            self.btn_energie_max = Button(self.window, text="Améliorer l'énergie max", command=lambda: self.ameliorer_energie_max(coder)) # On utilise un lambda car sinon ne peut pas passer le coder en arguments.
            self.btn_energie_max.pack()

            self.btn_niveau_codage = Button(self.window, text="Améliorer le niveau de codage", command=lambda: self.ameliorer_niveau_codage(coder))
            self.btn_niveau_codage.pack()
            coder.ResetEnergy()

        self.draw()
        self.draw_coder(coder)


    def draw(self):
        self.draw_info_missions()
        self.draw_infos_coder()
        self.draw_missions()    
     
    def draw_coder(self, coder):
        coder.Draw(self.canvas, self.CELL_SIZE)
    
    def play(self):
        self.draw()
        for coder in self.game.liste_coder:
            self.draw_coder(coder)
        self.window.mainloop()

    def display_end(self):
         self.canvas.create_text(10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                text="GAME OVER",
                                font=("Arial", 50),  # Exemple de police et de taille de texte
                                fill="red") 