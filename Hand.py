from Position import HandPosition
from dataStructures import Card
from dataStructures import CardType
from DrawingAndTrashPile import DrawingAndTrashPile

class Hand:

    def __init__(self, playerIdx : int, currentHand : dict[int,Card], drawingAndTrashPile : DrawingAndTrashPile):
        self.playerIdx = playerIdx
        self.pickedCards = []
        self.currentHand = currentHand
        self.drawingAndTrashPile = drawingAndTrashPile  #toto sem spadne z Game() pri inicializacii

    def pickCards(self, positions : list[HandPosition]) ->  list[Card]:   #
        out = []
        for pos in positions:
            out.append(self.currentHand[pos.getCardIndex()])

        self.pickedCards = out
        return out

    def removePickedCardsAndRedraw(self) -> list[Card]:
         return self.drawingAndTrashPile.discardAndDraw(self.pickedCards)

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


a = Hand(1,{1:Card(CardType(1),5)},DrawingAndTrashPile([Card(CardType(1),6),Card(CardType(1),4)], []))
#print(a.getCards())