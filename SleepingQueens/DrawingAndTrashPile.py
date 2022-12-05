from SleepingQueens.dataStructures import Card
import random

class DrawingAndTrashPile:

    def __init__(self, drawingPile : list[Card], trashPile : list[Card]):
        self.drawingPile = drawingPile
        self.trashPile = trashPile
        self.discardtedThisTurn : list[Card] = []

    def discardAndDraw(self, discard : list[Card], discard_before_shuffle : int = 3) -> list[Card]:

        output = []

        #OCP solution for handling shuffle of cards
        if len(discard) > len(self.drawingPile):
            # discard
            for i in range(discard_before_shuffle):
                temp_vymaz = discard.pop(0)
                self.trashPile.append(temp_vymaz)
                self.discardtedThisTurn.append(temp_vymaz)
                output.append(self.drawingPile.pop(0))

            # shuffle
            random.shuffle(self.trashPile)
            self.drawingPile = self.drawingPile + self.trashPile
            self.trashPile = []

            while discard != []:
                temp_vymaz = discard.pop(0)
                self.trashPile.append(temp_vymaz)
                self.discardtedThisTurn.append(temp_vymaz)
                output.append(self.drawingPile.pop(0))

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