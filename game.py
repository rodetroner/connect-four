from tkinter import *
from mechanics import *

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

class Board:
    def __init__(self, master):
        self.frame = Frame(master)
        self.game_running = True
        self.frame.pack()

        self.red_disc_img = PhotoImage(file='graphics/red_disc.gif')
        self.yellow_disc_img = PhotoImage(file='graphics/yellow_disc.gif')
        self.null_disc_img = PhotoImage(file='graphics/null_disc.gif')
        self.arrow_img = PhotoImage(file='graphics/arrow.gif')
        self.squares = []
        self.label = Label(self.frame, text='Tura gracza 1')
        self.label.grid(row=9, column=8)
        self.label2 = Label(self.frame, text='')
        self.label2.grid(row=8, column=8)



    def setup(self, game):
        '''Setup the game'''
        game.__init__()
        # put buttons in the window, but only the topmost row has commands
        # assigned
        for c in range(BOARD_WIDTH):
            column = []
            button = Button(self.frame, image=self.arrow_img,
                command=lambda c = c: game.addDisc(c))
            button.grid(row=0, column=c)
            column.append(button)
            for r in range(1, BOARD_HEIGHT):
                button = Button(self.frame, image=self.null_disc_img)
                button.grid(row=r, column=c)
                column.append(button)
            self.squares.append(column)
        
        root.after(10, board.update, game)

    def restart(self, window, game, root):
        '''Restart the game'''
        window.destroy()
        self.restart_game = True
        

    def end(self, game, root):
        '''End the game'''
        victory = Tk()
        frame = Frame(victory)
        frame.pack()
        label = Label(frame, text=self.victory_message)
        label.pack()
        button = Button(frame, text="Zagraj jeszcze raz",
            command=lambda: self.restart(victory, game, root))
        button.pack()

        
    def update(self, game):
        '''Check if the state of the game has changed and react accordingly'''
        for disc in game.getDiscs():
            if disc.getColor() == 'red':
                self.squares[disc.getX()][disc.getY()].config(image=self.red_disc_img)
            elif disc.getColor() == 'yellow':
                self.squares[disc.getX()][disc.getY()].config(image=self.yellow_disc_img)

        if game.getCurrentPlayer() == 'red':
            self.label.config(text='Tura gracza 1')
        else:
            self.label.config(text='Tura gracza 2')

        if game.isWon():
            if game.getCurrentPlayer() == 'red':
                self.victory_message="wygrał gracz 2"
            else:
                self.victory_message="wygrał gracz 1"
            self.game_running = False
            self.end(game, root)
        
        if game.isTied():
            self.label.config(text="PAT")

        if game.tooHigh():
            self.label2.config(text="Kolumna zapełniona")
        else:
            self.label2.config(text="                              ")

        if self.game_running:
            root.after(15, self.update, game)

root = Tk()
root.title(string='Connect Four')
game = Game()

board = Board(root)
board.setup(game)

root.mainloop()
