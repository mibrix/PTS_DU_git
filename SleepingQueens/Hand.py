from SleepingQueens.Position import HandPosition
from SleepingQueens.dataStructures import Card
from SleepingQueens.dataStructures import CardType
from SleepingQueens.DrawingAndTrashPile import DrawingAndTrashPile
from SleepingQueens.DrawingAndTrashPile import DiscardAll


class Hand:

    def __init__(self, playerIdx : int, currentHand : dict[int,Card], drawingAndTrashPile : DrawingAndTrashPile):
        self.playerIdx = playerIdx
        self.pickedCards : list[Card]
        self.currentHand = currentHand
        self.drawingAndTrashPile = drawingAndTrashPile  #toto sem spadne z Game() pri inicializacii

    def pickCards(self, positions : list[HandPosition]) ->  list[Card]:   #
        out = []
        for pos in positions:
            out.append(self.currentHand[pos.getCardIndex()])

        self.pickedCards = out
        return out

    def removePickedCardsAndRedraw(self) -> list[Card]:
         return self.drawingAndTrashPile.discardAndDraw(self.pickedCards,
                                                        DiscardAll(self.drawingAndTrashPile.drawingPile,
                                                                   self.drawingAndTrashPile.trashPile,
                                                                   self.returnPickedCards(),))
    def returnPickedCards(self):
        return self.pickedCards

    def hasCardOfType(self, type : CardType):
        for index,card in self.currentHand.items():
            if type == card.type:
                return HandPosition(index, self.playerIdx)
        #ak nema hrac danu kartu
        return HandPosition(-1, -1)

    def getCards(self):
        return [i for i in self.currentHand.values()]
