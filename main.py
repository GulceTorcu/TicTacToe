from Board import *
from Player import *

class main():

    board=Board()
    px=Player("X")
    po=Player("O")
    result=0
    tie=1

    board.printHelp()
    while result==0 and tie>0:
        board.updateBoard(px.mark)
        result=board.checkWin()
        tie=board.checkTie()
        if result==1 or tie==0:
            break
        board.updateBoard(po.mark)
        result = board.checkWin()
