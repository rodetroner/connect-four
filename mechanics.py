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

    def addCoin(self, x, y, color):
        self.coins.append(Coin(x, y, color))
