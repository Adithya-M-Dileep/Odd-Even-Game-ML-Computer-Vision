class GameController:
    def __init__(self):
        self.aiPoints = 0
        self.humanPoints = 0
        self.aiTurn = True
        self.GameEnded = False

    def getAiPoints(self):
        return int(self.aiPoints)

    def setAiPoints(self, points):
        self.aiPoints += points

    def getHumanPoints(self):
        return int(self.humanPoints)

    def setHumanPoints(self, points):
        self.humanPoints += points

    def play(self, ai, human):
        if self.GameEnded:
            return
        if self.aiTurn:
            if ai == human:
                self.aiTurn = False
            else:
                self.setAiPoints(ai)
        else:
            if ai == human:
                self.GameEnded = True
            else:
                self.setHumanPoints(human)

            if self.aiPoints < self.humanPoints:
                self.GameEnded = True

    def getWinner(self):
        if self.aiPoints > self.humanPoints:
            return ["AI WON", (255, 0, 0)]
        elif self.aiPoints < self.humanPoints:
            return ["YOU WON", (0, 0, 255)]
        else:
            return ["Tie", (0, 255, 0)]
