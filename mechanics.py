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

    def addCoin(self, column):
        self.coins.append(Coin(column, 11, self.current_player))
 #       print(self.coins)

