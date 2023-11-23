
Board= []

def InitBoard():
    global Board
    print("")
    print("------- Niveau 0 ------- : ")  
    print("")

    Board = [["  " for x in range(21)] for y in range(21)]     # Création d'une grille 21 par 21 remplie de zéros
    Board[10][10] = "JC"
    return Board
 
def AfficherBoard(Board):
    for i in range(len(Board)):
        print("\n" + " | " + " | ".join(Board[i]) + " | " + "\n")


InitBoard()
AfficherBoard(Board)        