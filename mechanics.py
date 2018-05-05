MIN_HEIGHT= 6

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
        self.current_turn = 0
        self.current_player = 'red'

    def nextTurn(self):
        if self.current_player == 'red':
            self.current_player = 'blue'
        else:
            self.current_player = 'red'

    def getBottomFreeHoleInColumn(self, column):
        lowest = MIN_HEIGHT
        for coin in self.coins:
            if coin.getX() == column:
                if coin.getY() <= lowest:
                    lowest = coin.getY()-1

        return lowest

    def addCoin(self, column):
        row = self.getBottomFreeHoleInColumn(column)
        self.coins.append(Coin(column, row, self.current_player))
        self.nextTurn()

