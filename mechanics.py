MIN_HEIGHT= 5
BOARD_WIDTH = 7
BOARD_HEIGHT= 5


class Coin:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def __str__(self):
        return 'Coin: x=' + str(self.x) + ', y=' + str(self.y) + ', color='\
            + self.color

    def __repr__(self):
        return 'Coin(' + str(self.x) + ', ' + str(self.y) + ', '\
            + self.color + ')'



class Game:
    def __init__(self):
        self.coins = []
        self.current_player = 'red'

    def nextTurn(self):
        if self.current_player == 'red':
            self.current_player = 'yellow'
        else:
            self.current_player = 'red'

    def southConnect(self, new, distance):
        for old in self.coins:
            if new.getColor() == old.getColor():
                if new.getX() == old.getX() and new.getY()+distance == old.getY():
                    return True

    def westConnect(self, new, distance):
        for old in self.coins:
            if new.getColor() == old.getColor():
                if new.getY() == old.getY() and new.getX()-distance == old.getX():
                    return True

    def eastConnect(self, new, distance):
        for old in self.coins:
            if new.getColor() == old.getColor():
                if new.getY() == old.getY() and new.getX()+distance == old.getX():
                    return True

    def northWestConnect(self, new, distance):
        for old in self.coins:
            if new.getColor() == old.getColor():
                if new.getY()+distance == old.getY() and new.getX()+distance == old.getX():
                    return True

    def northEastConnect(self, new, distance):
        for old in self.coins:
            if new.getColor() == old.getColor():
                if new.getY()+distance == old.getY() and new.getX()-distance == old.getX():
                    return True

    def checkForTie(self):
        if len(self.coins) == BOARD_HEIGHT * BOARD_WIDTH:
            return True
        else:
            return False


    def checkForLines(self):
        for coin in self.coins:
            if self.southConnect(coin, 1):
                if self.southConnect(coin, 2):
                    if self.southConnect(coin, 3):
                        return True

            if self.westConnect(coin, 1):
                if self.westConnect(coin, 2):
                    if self.westConnect(coin, 3):
                        return True

            if self.eastConnect(coin, 1):
                if self.eastConnect(coin, 2):
                    if self.eastConnect(coin, 3):
                        return True

            if self.northWestConnect(coin, 1):
                if self.northWestConnect(coin, 2):
                    if self.northWestConnect(coin, 3):
                        return True

            if self.northEastConnect(coin, 1):
                if self.northEastConnect(coin, 2):
                    if self.northEastConnect(coin, 3):
                        return True

        return False
        

    def getBottomFreeHoleInColumn(self, column):
        lowest = MIN_HEIGHT
        for coin in self.coins:
            if coin.getX() == column:
                if coin.getY() <= lowest:
                    lowest = coin.getY()-1

        return lowest


    def addCoin(self, column):
        row = self.getBottomFreeHoleInColumn(column)
        if row != 0:
            self.coins.append(Coin(column, row, self.current_player))
        else:
            print("NNNNNNNNNNNNNOOOOOOOOOOO")
        if self.checkForTie():
            print("TIE POTATO")
        if self.checkForLines():
            print("YA BOI")
        self.nextTurn()


    def getCoins(self):
        return self.coins


