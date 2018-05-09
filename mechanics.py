MIN_HEIGHT= 5
BOARD_WIDTH = 7
BOARD_HEIGHT= 5


class Disc:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getX(self):
        '''Get x position of the disc'''
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def __str__(self):
        return 'Disc: x=' + str(self.x) + ', y=' + str(self.y) + ', color='\
            + self.color

    def __repr__(self):
        return 'Disc(' + str(self.x) + ', ' + str(self.y) + ', '\
            + self.color + ')'



class Game:
    def __init__(self):
        self.discs = []
        self.current_player = 'red'
        self.game_won = False
        self.game_tied = False
        self.too_high = False

    def nextTurn(self):
        '''Change the current player'''
        if self.current_player == 'red':
            self.current_player = 'yellow'
        else:
            self.current_player = 'red'
        self.too_high = False

    def southConnect(self, new, distance):
        for old in self.discs:
            if new.getColor() == old.getColor():
                if new.getX() == old.getX() and new.getY()+distance == old.getY():
                    return True

    def westConnect(self, new, distance):
        for old in self.discs:
            if new.getColor() == old.getColor():
                if new.getY() == old.getY() and new.getX()-distance == old.getX():
                    return True

    def eastConnect(self, new, distance):
        for old in self.discs:
            if new.getColor() == old.getColor():
                if new.getY() == old.getY() and new.getX()+distance == old.getX():
                    return True

    def northWestConnect(self, new, distance):
        for old in self.discs:
            if new.getColor() == old.getColor():
                if new.getY()+distance == old.getY() and new.getX()+distance == old.getX():
                    return True

    def northEastConnect(self, new, distance):
        for old in self.discs:
            if new.getColor() == old.getColor():
                if new.getY()+distance == old.getY() and new.getX()-distance == old.getX():
                    return True

    def checkForTie(self):
        if len(self.discs) == BOARD_HEIGHT * BOARD_WIDTH:
            return True
        else:
            return False


    def checkForWin(self):
        for disc in self.discs:
            if self.southConnect(disc, 1):
                if self.southConnect(disc, 2):
                    if self.southConnect(disc, 3):
                        return True

            if self.westConnect(disc, 1):
                if self.westConnect(disc, 2):
                    if self.westConnect(disc, 3):
                        return True

            if self.eastConnect(disc, 1):
                if self.eastConnect(disc, 2):
                    if self.eastConnect(disc, 3):
                        return True

            if self.northWestConnect(disc, 1):
                if self.northWestConnect(disc, 2):
                    if self.northWestConnect(disc, 3):
                        return True

            if self.northEastConnect(disc, 1):
                if self.northEastConnect(disc, 2):
                    if self.northEastConnect(disc, 3):
                        return True

        return False

    def getBottomFreeHoleInColumn(self, column):
        lowest = MIN_HEIGHT
        for disc in self.discs:
            if disc.getX() == column:
                if disc.getY() <= lowest:
                    lowest = disc.getY()-1

        return lowest

    def addDisc(self, column):
        row = self.getBottomFreeHoleInColumn(column)
        if row == 0:
            self.too_high = True
            return
        else:
            self.discs.append(Disc(column, row, self.current_player))
        if self.checkForWin():
            self.game_won = True
        if self.checkForTie():
            self.game_tied = True
        self.nextTurn()

    def getCurrentPlayer(self):
        return self.current_player

    def isWon(self):
        return self.game_won

    def isTied(self):
        return self.game_tied

    def tooHigh(self):
        return self.too_high

    def getDiscs(self):
        return self.discs


