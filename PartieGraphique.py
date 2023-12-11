from re import A
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

        self.window = Tk()
        self.window.title("ESN GAME")

        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()


        self.draw_board()  # Appel de la methode draw_board() pour dessiner la grille d�s la creation de la fenetre
        

        
        self.canvas.bind_all('<KeyPress>', self.move_coder)

        self.missions_label = Label(self.window, text="")
        self.coder_label = Label(self.window, text="")
        
        # Place le texte "JC" au milieu de la position (10, 10)
        self.canvas.create_text(10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                text="JC",
                                font=("Arial", 20),  # Exemple de police et de taille de texte
                                fill="black")  # Couleur du texte (ici noir)

        
        for i in range (self.HEIGHT):
            self.canvas.create_text(0 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                i * self.CELL_SIZE + self.CELL_SIZE // 2,
                                text="X",
                                font=("Arial", 20),  # Exemple de police et de taille de texte
                                fill="black")  # Couleur du texte (ici noir)

        for i in range(self.NB_CELL_WIDTH):
            self.canvas.create_text(i * self.CELL_SIZE + self.CELL_SIZE // 2,
                            0 * self.CELL_SIZE + self.CELL_SIZE // 2,
                            text="X",
                            font=("Arial", 20),
                            fill="black")


        
        
        self.round = 0
        
    def afficher_info_missions(self, liste_missions):
        # Cr�ation de la cha�ne de texte pour les informations sur les missions
        mission_info_text = "Liste des missions :\n"
        mission_info_text = AfficherInfosMissions(liste_missions)

        self.missions_label.destroy()
        self.missions_label = Label(self.window, text=mission_info_text)
        # Cr�ation du label avec les informations des missions
        #mission_info_label = Label(self.window, text=mission_info_text)
        self.missions_label.pack(side="right",anchor="n", padx=10, pady=10)
        #self.mission_info_label.text = mission_info_text
        
    def afficher_infos_coder(self,liste_coder):
        # Creation de la chaine de texte pour les informations sur le coder
        mission_info_text = "Infos coder(s) :\n"
        mission_info_text = AfficherInfosCoder(liste_coder)

        self.coder_label.destroy()
        self.coder_label = Label(self.window, text=mission_info_text)
        
        # Cr�ation du label avec les informations des missions
        self.coder_label.pack(side="left",anchor="n", fill='y', padx=10, pady=10)

        
    
    def draw_board(self):
        for i in range(self.NB_CELL_HEIGHT ):
            for j in range(self.NB_CELL_WIDTH):
                x1 = i * self.CELL_SIZE
                y1 = j * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
        



    def draw_missions(self, liste_missions):
        
        for mission in liste_missions:
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
            

            self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='yellow')
            self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=f"{mission_number}", fill='black')

    def ameliorer_energie_max(self,coder):

        if CoutDepenseArgentAuJobCenterPourEnergyMax(coder):
            coder.UpgradeEnergyMax()
            print("Bien Améliorer l'énergie maximale")

    def ameliorer_niveau_codage(self,coder):

         if CoutDepenseArgentAujobCenterPourCodingLevel(coder):
            coder.UpgradeCodingLevel()
            print("Bien Améliorer le niveau de codage")
           
    
    def move_coder(self, event):
        
        keyPressed = event.keysym
        moveDirection = (0, 0)
        current_coder_index = (self.round + 1) % self.game.nb_coder
        coder = self.game.liste_coder[current_coder_index]
        
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


        if CheckJobCenter(self.game.Board, coder):

            self.btn_energie_max = Button(self.window, text="Améliorer l'énergie max", command=lambda: self.ameliorer_energie_max(coder))
            self.btn_energie_max.pack()

            self.btn_niveau_codage = Button(self.window, text="Améliorer le niveau de codage", command=lambda: self.ameliorer_niveau_codage(coder))
            self.btn_niveau_codage.pack()
            coder.ResetEnergy()

                
        self.draw()

    

    def draw(self):
        
        for coder in self.game.liste_coder:
            coder.Draw(self.canvas, self.CELL_SIZE)
 
        self.draw_missions(self.game.liste_missions) 
        self.afficher_info_missions(self.game.liste_missions)
        self.afficher_infos_coder(self.game.liste_coder)
