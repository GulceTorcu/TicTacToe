
class Board():
    def __init__(self):
        self.pos=[" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def printBoard(self):
        print(" "+self.pos[0]+" | "+self.pos[1]+" | "+self.pos[2]+" ")
        print("-----------")
        print(" "+self.pos[3]+" | "+self.pos[4]+" | "+self.pos[5]+" ")
        print("-----------")
        print(" "+self.pos[6]+" | "+self.pos[7]+" | "+self.pos[8]+" ")

    def printHelp(self):
        print("Locations are below")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 " )
        print("-----------")
        print(" 7 | 8 | 9 ")

    def updateBoard(self,mark):
        choice=int(input("Write position for " +mark+ ": "))
        choice=choice-1
        if choice<9 and choice>=0:
            if self.pos[choice]== " ":
                self.pos[choice]=mark
                Board.printBoard(self)
            else:
                print("Already full, Player" + mark + "lost turn")
        else:
            print("Ghoose between 1-9, Player" + mark + "lost turn")

    def checkWin(self):
        result=0
        winningConditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (6, 4, 2), (8, 4, 0), (6, 3, 0), (7, 4, 1), (8, 5, 2)]
        for i in winningConditions:
            if self.pos[i[0]]==self.pos[i[1]]==self.pos[i[2]]:
                if self.pos[i[0]]=="X" or self.pos[i[0]]=="O":
                    print("Win for Player " +self.pos[i[0]])
                    result=result+1
        return result

    def checkTie(self):
        tie=0
        for i in range(9):
            if self.pos[i]==" ":
                tie=tie+1
        return tie