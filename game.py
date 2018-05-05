from tkinter import *

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

class Game:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()

        self.red_coin_img = PhotoImage(file='red_coin.gif')
        self.yellow_coin_img = PhotoImage(file='yellow_coin.gif')
        self.null_coin_img = PhotoImage(file='null_coin.gif')

        self.squares = []

        for c in range(BOARD_WIDTH):
            column = []
            for r in range(BOARD_HEIGHT):
                button = Button(self.frame, image=self.null_coin_img)
                button.grid(row=r, column=c)
                column.append(button)
            self.squares.append(column)

root = Tk()

game = Game(root)

root.mainloop()
