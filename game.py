from tkinter import *
from mechanics import *

class TitleScreen:
    def __init__(self, master):
        self._master = master
        self._frame = Frame(master)
        self._options = ['4-in-a-row', '5-in-a-row']
        self._frame.pack()

        self._label = Label(self._frame, text="Wybierz tryb gry")
        self._label.grid(row=0, column=0)

        self._variable = StringVar(master)
        self._variable.set(self._options[0])
        self._menu = OptionMenu(self._frame, self._variable, *self._options)
        self._menu.grid(row=1, column=0)

        self._button = Button(self._frame, text="Rozpocznij grę",
            command=lambda: self.startGame(self._variable.get()))
        self._button.grid(row=2, column=0)

    def startGame(self, option):
        self._frame.destroy()
        if option == '4-in-a-row':
            game = fourInARow()
            board = GUI(self._master, game)
            board.setup()

        elif option == '5-in-a-row':
            game = fiveInARow()
            board = GUI(self._master, game)
            board.setup()



class GUI:
    def __init__(self, master, game):
        self._frame = Frame(master)
        self._game_running = True
        self._current_game = game
        self._frame.pack()

        self._red_disc_img = PhotoImage(file='graphics/red_disc.gif')
        self._yellow_disc_img = PhotoImage(file='graphics/yellow_disc.gif')
        self._null_disc_img = PhotoImage(file='graphics/null_disc.gif')
        self._red_arrow_img = PhotoImage(file='graphics/red_arrow.gif')
        self._yellow_arrow_img = PhotoImage(file='graphics/yellow_arrow.gif')
        self._squares = []
        self._game_state_label = Label(self._frame, text='Tura gracza 1')
        self._game_state_label.grid(row=3,
            column=self._current_game.getWidth()+1)
        self._restart_button = Button(self._frame, text="Restart",
            command=lambda: self.restart(root))
        self._restart_button.grid(row=1,
            column=self._current_game.getWidth()+1)
        self._full_column_label = Label(self._frame, text='')
        self._full_column_label.grid(row=4, column=self._current_game.getWidth()+1)

    def setup(self):
        '''Setup the game'''
        self._current_game.__init__()
        # put buttons in the window, but only the topmost row has commands
        # assigned
        for c in range(self._current_game.getWidth()):
            column = []
            button = Button(self._frame, image=self._red_arrow_img,
                command=lambda c = c: self._current_game.addDisc(c))
            button.grid(row=0, column=c)
            column.append(button)
            for r in range(1, self._current_game.getHeight()+1):
                button = Button(self._frame, image=self._null_disc_img)
                button.grid(row=r, column=c)
                column.append(button)
            self._squares.append(column)
        
        root.after(15, self.update)


    def restart(self, root, window=None):
        '''Restart the game'''
        if window is not None:
            window.destroy()
        self._frame.destroy()
        self.__init__(root, self._current_game)
        self.setup()


    def end(self, root):
        '''End the game'''
        victory = Tk()
        frame = Frame(victory)
        frame.pack()
        end_game_label = Label(frame, text=self._victory_message)
        end_game_label.pack()
        button = Button(frame, text="Zagraj jeszcze raz",
            command=lambda: self.restart(root, victory))
        button.pack()
        

    def update(self):
        '''Check if the state of the game has changed and react accordingly'''

        # Check if there are new discs to be added to the board
        # and change graphics of appropriate buttons
        for disc in self._current_game.getDiscs():
            if disc.getColor() == 'red':
                self._squares[disc.getX()][disc.getY()].config(image=self._red_disc_img)
            elif disc.getColor() == 'yellow':
                self._squares[disc.getX()][disc.getY()].config(image=self._yellow_disc_img)

        # Display current player
        if self._current_game.getCurrentPlayer() == 'red':
            self._game_state_label.config(text='Tura gracza 1')
            for i in range(self._current_game.getWidth()):
                self._squares[i][0].config(image=self._red_arrow_img)
        else:
            self._game_state_label.config(text='Tura gracza 2')
            for i in range(self._current_game.getWidth()):
                self._squares[i][0].config(image=self._yellow_arrow_img)

        if self._current_game.isWon():
            if self._current_game.getCurrentPlayer() == 'red':
                self._victory_message = "Wygrał gracz 2"
            else:
                self._victory_message = "Wygrał gracz 1"
            self._game_running = False
            self.end(root)
        
        if self._current_game.isTied():
            self._victory_message = "Remis"
            self._game_running = False
            self.end(root)

        # Check if player wants to put a disc in a full column
        if self._current_game.tooHigh():
            self._full_column_label.config(text="Kolumna zapełniona")
        else:
            self._full_column_label.config(text="                              ")

        if self._game_running:
            root.after(15, self.update)

root = Tk()
root.title(string='Connect Four')

TitleScreen(root)

root.mainloop()
