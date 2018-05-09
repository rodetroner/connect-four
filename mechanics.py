MIN_HEIGHT= 5
BOARD_WIDTH = 7
BOARD_HEIGHT= 5


class Disc:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getX(self):
        '''Get x position of a disc'''
        return self.x

    def getY(self):
        '''Get y position of a disc'''
        return self.y

    def getColor(self):
        '''Get color of a disc'''
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

    def southConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        south'''
        for old_disc in self.discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getX() == old_disc.getX() \
                    and new_disc.getY()+distance == old_disc.getY():
                    return True

    def westConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        west'''
        for old_disc in self.discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY() == old_disc.getY() \
                    and new_disc.getX()-distance == old_disc.getX():
                    return True

    def eastConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        east'''
        for old_disc in self.discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY() == old_disc.getY() \
                    and new_disc.getX()+distance == old_disc.getX():
                    return True

    def northWestConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        north-west'''
        for old_disc in self.discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY()+distance == old_disc.getY() \
                    and new_disc.getX()+distance == old_disc.getX():
                    return True

    def northEastConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        nort-east'''
        for old_disc in self.discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY()+distance == old_disc.getY() \
                    and new_disc.getX()-distance == old_disc.getX():
                    return True

    # There's no need to check for any other direction because the disc rise
    # upward

    def checkForTie(self):
        '''Check if the board is filled with discs which mean tie'''
        if len(self.discs) == BOARD_HEIGHT * BOARD_WIDTH:
            return True
        else:
            return False


    def checkForWin(self):
        '''Check for every disc if it has 3 connecting disc of the same color
        in any direction which means a win for the player having this color'''
        
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
        '''Get the y position of the first free hole, counting up, in given
        column'''
        lowest = MIN_HEIGHT
        for disc in self.discs:
            if disc.getX() == column:
                if disc.getY() <= lowest:
                    lowest = disc.getY()-1

        return lowest

    def addDisc(self, column):
        '''Put a disc in given column and check if any ending condition has
        been met'''
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


