from tkinter import *
from mechanics import *

BOARD_WIDTH = 7
BOARD_HEIGHT = 7

class Board:
    def __init__(self, master, game):
        self.frame = Frame(master)
        self.game_running = True
        self.current_game = game
        self.frame.pack()

        self.red_disc_img = PhotoImage(file='graphics/red_disc.gif')
        self.yellow_disc_img = PhotoImage(file='graphics/yellow_disc.gif')
        self.null_disc_img = PhotoImage(file='graphics/null_disc.gif')
        self.arrow_img = PhotoImage(file='graphics/arrow.gif')
        self.squares = []
        self.game_state_label = Label(self.frame, text='Tura gracza 1')
        self.game_state_label.grid(row=9, column=8)
        self.full_column_label = Label(self.frame, text='')
        self.full_column_label.grid(row=8, column=8)

    def setup(self):
        '''Setup the game'''
        self.current_game.__init__()
        # put buttons in the window, but only the topmost row has commands
        # assigned
        for c in range(BOARD_WIDTH):
            column = []
            button = Button(self.frame, image=self.arrow_img,
                command=lambda c = c: self.current_game.addDisc(c))
            button.grid(row=0, column=c)
            column.append(button)
            for r in range(1, BOARD_HEIGHT):
                button = Button(self.frame, image=self.null_disc_img)
                button.grid(row=r, column=c)
                column.append(button)
            self.squares.append(column)
        
        root.after(15, self.update)


    def restart(self, window, root):
        '''Restart the game'''
        window.destroy()
        self.frame.destroy()
        self.__init__(root, self.current_game)
        self.setup()


    def end(self, root):
        '''End the game'''
        victory = Tk()
        frame = Frame(victory)
        frame.pack()
        end_game_label = Label(frame, text=self.victory_message)
        end_game_label.pack()
        button = Button(frame, text="Zagraj jeszcze raz",
            command=lambda: self.restart(victory, root))
        button.pack()
        

    def update(self):
        '''Check if the state of the game has changed and react accordingly'''

        # Check if there are new discs to be added to the board
        # and change graphics of appropriate buttons
        for disc in self.current_game.getDiscs():
            if disc.getColor() == 'red':
                self.squares[disc.getX()][disc.getY()].config(image=self.red_disc_img)
            elif disc.getColor() == 'yellow':
                self.squares[disc.getX()][disc.getY()].config(image=self.yellow_disc_img)

        # Display current player
        if self.current_game.getCurrentPlayer() == 'red':
            self.game_state_label.config(text='Tura gracza 1')
        else:
            self.game_state_label.config(text='Tura gracza 2')

        if self.current_game.isWon():
            if self.current_game.getCurrentPlayer() == 'red':
                self.victory_message = "Wygrał gracz 2"
            else:
                self.victory_message = "Wygrał gracz 1"
            self.game_running = False
            self.end(root)
        
        if self.current_game.isTied():
            self.victory_message = "Remis"
            self.game_running = False
            self.end(root)

        # Check if player wants to put a disc in a full column
        if self.current_game.tooHigh():
            self.full_column_label.config(text="Kolumna zapełniona")
        else:
            self.full_column_label.config(text="                              ")

        if self.game_running:
            root.after(15, self.update)

root = Tk()
root.title(string='Connect Four')
game = fiveInARow()

board = Board(root, game)
board.setup()

root.mainloop()
