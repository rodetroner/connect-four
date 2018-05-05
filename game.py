from tkinter import *
from mechanics import *

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

class Board:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()

        self.red_coin_img = PhotoImage(file='red_coin.gif')
        self.yellow_coin_img = PhotoImage(file='yellow_coin.gif')
        self.null_coin_img = PhotoImage(file='null_coin.gif')
        self.squares = []

    def updateBoard(self):
        pass
        
game = Game()
root = Tk()

board = Board(root)
for c in range(BOARD_WIDTH):
    column = []
    button = Button(board.frame, image=board.red_coin_img,
        command=lambda c = c: game.addCoin(c))
    button.grid(row=0, column=c)
    column.append(button)
    for r in range(1, BOARD_HEIGHT):
        button = Button(board.frame, image=board.null_coin_img)
        button.grid(row=r, column=c)
        column.append(button)
    board.squares.append(column)

root.mainloop()
