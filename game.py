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
            for r in range(1, BOARD_HEIGHT):
                label = Label(image=self.red_coin_img)
                label.grid(row=r, column=c)
                column.append(label)
            self.squares.append(column)



root = Tk()

game = Game(root)

root.mainloop()
