from tkinter import *
from mechanics import *

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

class Board:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.red_coin_img = PhotoImage(file='red_coin.gif')
        self.yellow_coin_img = PhotoImage(file='yellow_coin.gif')
        self.null_coin_img = PhotoImage(file='null_coin.gif')
        self.squares = []
        self.label = Label(self.frame, text='Tura gracza 1')
        self.label.grid(row=11, column=8)
        self.label2 = Label(self.frame, text="")
        self.label.grid(row=11, column=9)



    def setup(self, game):
        for c in range(BOARD_WIDTH):
            column = []
            button = Button(self.frame, image=self.red_coin_img,
            command=lambda c = c: game.addCoin(c))
            button.grid(row=0, column=c)
            column.append(button)
            for r in range(1, BOARD_HEIGHT):
                button = Button(self.frame, image=self.null_coin_img)
                button.grid(row=r, column=c)
                column.append(button)
            self.squares.append(column)
    def update(self, game):
        for coin in game.getCoins():
            if coin.getColor() == 'red':
                self.squares[coin.getX()][coin.getY()].config(image=self.red_coin_img)
            elif coin.getColor() == 'yellow':
                self.squares[coin.getX()][coin.getY()].config(image=self.yellow_coin_img)

        if game.getCurrentPlayer() == 'red':
            self.label.config(text='Tura gracza 1')
        else:
            self.label.config(text='Tura gracza 2')

        if game.isWon():
            if game.getCurrentPlayer() == 'red':
                self.label.config(text="wygrał gracz 2")
            else:
                self.label.config(text="wygrał gracz 1")
        
        if game.isTied():
            self.label.config(text="PAT")

        if game.tryingToPlaceTooHigh():
            self.label2.config("Kolumna zapełniona")

        root.after(10, self.update, game)

    def checkForResults(self, game):
        pass

root = Tk()
root.title(string='Connect Four')
game = Game()

board = Board(root)
board.setup(game)
root.after(10, board.update, game)

root.mainloop()
