MIN_HEIGHT= 6
BOARD_WIDTH = 7
BOARD_HEIGHT= 6


class Disc:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def getX(self):
        '''Get x position of a disc'''
        return self._x

    def getY(self):
        '''Get y position of a disc'''
        return self._y

    def getColor(self):
        '''Get color of a disc'''
        return self._color

    def __str__(self):
        return 'Disc: x=' + str(self._x) + ', y=' + str(self._y) + ', color='\
            + self._color

    def __repr__(self):
        return 'Disc(' + str(self._x) + ', ' + str(self._y) + ', '\
            + self._color + ')'

class Game:
    def __init__(self):
        self._discs = []
        self._current_player = 'red'
        self._too_high = False

    def nextTurn(self):
        '''Change the current player'''
        if self._current_player == 'red':
            self._current_player = 'yellow'
        else:
            self._current_player = 'red'
        self._too_high = False

    def southConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        south'''
        for old_disc in self._discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getX() == old_disc.getX() \
                    and new_disc.getY()+distance == old_disc.getY():
                    return True

    def westConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        west'''
        for old_disc in self._discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY() == old_disc.getY() \
                    and new_disc.getX()-distance == old_disc.getX():
                    return True

    def eastConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        east'''
        for old_disc in self._discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY() == old_disc.getY() \
                    and new_disc.getX()+distance == old_disc.getX():
                    return True

    def northWestConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        north-west'''
        for old_disc in self._discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY()+distance == old_disc.getY() \
                    and new_disc.getX()+distance == old_disc.getX():
                    return True

    def northEastConnect(self, new_disc, distance):
        '''Check if there's a disc of the same color at given distance to the
        nort-east'''
        for old_disc in self._discs:
            if new_disc.getColor() == old_disc.getColor():
                if new_disc.getY()+distance == old_disc.getY() \
                    and new_disc.getX()-distance == old_disc.getX():
                    return True

    # There's no need to check for any other direction because the disc rise
    # upward

    def isTied(self):
        '''Check if the board is filled with discs which mean tie'''
        if len(self._discs) == BOARD_HEIGHT * BOARD_WIDTH:
            return True
        else:
            return False


    def isWon(self):
        '''Check for every disc if it has 3 connecting disc of the same color
        in any direction which means a win for the player having this color'''
        
        for disc in self._discs:
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
        for disc in self._discs:
            if disc.getX() == column:
                if disc.getY() <= lowest:
                    lowest = disc.getY()-1

        return lowest

    def addDisc(self, column):
        '''Put a disc in given column'''
        row = self.getBottomFreeHoleInColumn(column)
        if row == 0:
            self._too_high = True
            return
        else:
            self._discs.append(Disc(column, row, self._current_player))
        self.nextTurn()

    def getCurrentPlayer(self):
        return self._current_player

    def tooHigh(self):
        return self._too_high

    def getDiscs(self):
        return self._discs


