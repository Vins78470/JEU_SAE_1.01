from tkinter import *
from Coder import *
from Mission import *
from Rules import AfficherInfosCoder, AfficherInfosMissions
from Game import *
# coding: utf-8



class WindowForGame:

    
    def __init__(self, game, cell_size=50, nb_cell_width=21, nb_cell_height=21):
      
        self.CELL_SIZE = cell_size
        self.NB_CELL_WIDTH = nb_cell_width
        self.NB_CELL_HEIGHT = nb_cell_height
        self.WIDTH = self.CELL_SIZE * self.NB_CELL_WIDTH
        self.HEIGHT = self.CELL_SIZE * self.NB_CELL_HEIGHT
          
        self.game = game

        self.window = Tk()
        self.window.title("ESN GAME")

        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()


        self.draw_board()  # Appel à la méthode draw_board() pour dessiner la grille dès la création de la fenêtre
    
        
        self.canvas.bind_all('<KeyPress>', self.move_coder)

        self.missions_label = Label(self.window, text="")
        self.coder_label = Label(self.window, text="")
        
        # Placer le texte "JC" au milieu à la position (10, 10)
        self.canvas.create_text(10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                10 * self.CELL_SIZE + self.CELL_SIZE // 2,
                                text="JC",
                                font=("Arial", 20),  # Exemple de police et de taille de texte
                                fill="black")  # Couleur du texte (ici noir)
        
        self.round = 0
        
    def afficher_info_missions(self, liste_missions):
        # Création de la chaîne de texte pour les informations sur les missions
        mission_info_text = "Liste des missions :\n"
        mission_info_text = AfficherInfosMissions(liste_missions)

        self.missions_label.destroy()
        self.missions_label = Label(self.window, text=mission_info_text)
        # Création du label avec les informations des missions
        #mission_info_label = Label(self.window, text=mission_info_text)
        self.missions_label.pack(side="right",anchor="n", fill='y', padx=10, pady=10)
        #self.mission_info_label.text = mission_info_text
        
    def afficher_infos_coder(self,liste_coder):
        # Création de la chaîne de texte pour les informations sur le coder
        mission_info_text = "Infos coder(s) :\n"
        mission_info_text = AfficherInfosCoder(liste_coder)

        self.coder_label.destroy()
        self.coder_label = Label(self.window, text=mission_info_text)
        
        # Création du label avec les informations des missions
        self.coder_label.pack(side="left",anchor="n", fill='y', padx=10, pady=10)

        
    # Draw initial rectangles
    def draw_board(self):
        for i in range(self.NB_CELL_HEIGHT):
            for j in range(self.NB_CELL_WIDTH):
                x1 = i * self.CELL_SIZE
                y1 = j * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
        



    def draw_missions(self, liste_missions):
        print("ca rentre")
        for mission in liste_missions:
            mission_x, mission_y = mission.GetPosition()  # Utiliser le getter pour obtenir la position de la mission

            mission_x *= self.CELL_SIZE
            mission_y *= self.CELL_SIZE

            x1 = mission_x
            y1 = mission_y
            x2 = mission_x + self.CELL_SIZE
            y2 = mission_y + self.CELL_SIZE

            self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='yellow')
           
    
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
        elif CheckJobCenter(self.game.Board, coder):
            if keyPressed == 'a':
                MakeChoiceAtJobCenter(coder, keyPressed)
            elif keyPressed == 'c':
                MakeChoiceAtJobCenter(coder, keyPressed)
                
        self.draw()

    def draw(self):
        for coder in self.game.liste_coder:
            coder.Draw(self.canvas, self.CELL_SIZE)
 
        self.draw_missions(self.game.liste_missions) 
        self.afficher_info_missions(self.game.liste_missions)
        self.afficher_infos_coder(self.game.liste_coder)
