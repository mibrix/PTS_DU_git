from SleepingQueens.dataStructures import Card
import random
from abc import ABC, abstractmethod

class DrawingStrategy(ABC):
    @abstractmethod
    def create_strategy(self):
        pass

class DiscardAll(DrawingStrategy):
    def __init__(self, drawingPile : list[Card], trashPile : list[Card], discard : list[Card]):
        self.drawingPile = drawingPile
        self.trashPile = trashPile
        self.discard = discard
        self.output :list[Card] = []

    def create_strategy(self) -> list[Card]:
        number_to_draw = len(self.discard)
        # discard
        for i in range(len(self.discard)):
            temp_vymaz = self.discard.pop(0)
            self.trashPile.append(temp_vymaz)
        #    self.discardtedThisTurn.append(temp_vymaz)

        number_of_drawn = 0
        while self.drawingPile != []:
            self.output.append(self.drawingPile.pop(0))
            number_of_drawn += 1

        # shuffle
        random.shuffle(self.trashPile)
        self.drawingPile = self.drawingPile + self.trashPile
        self.trashPile = []

        for i in range(number_to_draw - number_of_drawn):
            self.output.append(self.drawingPile.pop(0))

        return self.output


class ShuffleAndDiscard(DrawingStrategy):
    def __init__(self, drawingPile: list[Card], trashPile: list[Card], discard: list[Card]):
        self.drawingPile = drawingPile
        self.trashPile = trashPile
        self.discard = discard
        self.output : list[Card] = []

    def create_strategy(self) -> list[Card]:

        # shuffle
        random.shuffle(self.trashPile)
        self.drawingPile = self.drawingPile + self.trashPile
        self.trashPile = []

        # discard and redraw
        for i in range(len(self.discard)):
            temp_vymaz = self.discard.pop(0)
            self.trashPile.append(temp_vymaz)
            self.output.append(self.drawingPile.pop(0))

        return self.output

class DrawingAndTrashPile:

    def __init__(self, drawingPile : list[Card], trashPile : list[Card]):
        self.drawingPile = drawingPile
        self.trashPile = trashPile
        self.discardtedThisTurn : list[Card] = []

    def discardAndDraw(self, discard : list[Card], drawingStrategy : DrawingStrategy) -> list[Card]:

        #OCP solution for handling shuffle of cards
        if len(discard) > len(self.drawingPile):
            output = drawingStrategy.create_strategy()

        else:
            #discard
            for card in discard:
                self.trashPile.append(card)
                self.discardtedThisTurn.append(card)

            #draw new cards (number of these cards = number of discarded cards)
            output = []
            for i in range(len(discard)):
                output.append(self.drawingPile.pop(0))

        return output

    def newTurn(self):
        self.discardtedThisTurn = []

    def getCardsDiscardedThisTurn(self) -> list[Card]:
        return self.discardtedThisTurn