class SleepingQueenPosition:
    def __init__(self, cardIndex : int):
        self.cardIndex = cardIndex

    def getCardIndex(self) -> int:
        return self.cardIndex


class AwokenQueenPosition:
    def __init__(self, cardIndex: int, playerIndex: int):
        self.cardIndex = cardIndex
        self.playerIndex = playerIndex

    def getCardIndex(self) -> int:
        return self.cardIndex

    def getPlayerIndex(self) -> int:
        return self.playerIndex

class HandPosition:
    def __init__(self, cardIndex: int, playerIndex: int):
        self.cardIndex = cardIndex
        self.playerIndex = playerIndex

    def getCardIndex(self) -> int:
        return self.cardIndex

    def getPlayerIndex(self) -> int:
        return self.playerIndex