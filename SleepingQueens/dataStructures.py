from enum import Enum
from SleepingQueens.Position import SleepingQueenPosition
from SleepingQueens.Position import AwokenQueenPosition
from SleepingQueens.Position import HandPosition

class Queen:
    def __init__(self, points : int):
        self.points = points

class CardType(Enum):
    Number = 1
    King = 2
    Knight = 3
    SleepingPotion = 4
    Dragon = 5
    MagicWand = 6


class Card:
    def __init__(self, type : CardType, value : int):
        self.type = type
        self.value = value

class GameState:

    def __init__(self, numberOfPlayers : int, onTurn : int, sleepingQueens : set[SleepingQueenPosition],
                 cards : dict[HandPosition, Card], awokenQueens : dict[AwokenQueenPosition, Queen],
                 cardDiscardedLastTurn:list[Card]):
        self.numberOfPlayers = numberOfPlayers
        self.onTurn = onTurn
        self.sleepingQueens = sleepingQueens
        self.cards = cards
        self.awokenQueens = awokenQueens
        self.cardDiscardedLastTurn = cardDiscardedLastTurn

    def updateGameStateCards(self, removeHandPos : list[HandPosition], addHandPos : list[Card]):

        for y in range(len(removeHandPos)):
            for i in self.cards.keys():
                if (i.getCardIndex() == removeHandPos[y].getCardIndex() and
                        i.getPlayerIndex() == removeHandPos[y].getPlayerIndex()):
                    self.cards[i] = addHandPos[y]
                    break

    def updateGameStateAfterAttack(self, awQueenPos : AwokenQueenPosition, new_owner : int):
        to_pop = AwokenQueenPosition(-1,-1)
        temp_q = Queen(-1)
        for i in self.awokenQueens.keys():
            if (i.getCardIndex() == awQueenPos.getCardIndex() and
                    i.getPlayerIndex() == awQueenPos.getPlayerIndex()):
                to_pop = i
                temp_q = self.awokenQueens[i]
                break

        #vymaz kralovnu z awokenQueens daneho hraca
        if to_pop.cardIndex != -1 and temp_q.points != -1:
            self.awokenQueens.pop(to_pop)
            to_pop.playerIndex = new_owner

            #ak hrac iba uspava kralovnu
            if new_owner == -1:
                q_idx = 0
                if self.sleepingQueens != set():
                    q_idx = max([i.cardIndex for i in self.sleepingQueens]) + 1
                self.sleepingQueens.add(SleepingQueenPosition(q_idx))

            #ak hrac utoci na kralovnu druheho hraca
            else:
                if self.awokenQueens == {}:
                    to_pop.cardIndex = max([i.cardIndex for i in self.awokenQueens.keys()])+1
                else:
                    to_pop.cardIndex = 0

                self.awokenQueens[to_pop] = temp_q

class PlayerState:
    def __init__(self, cards : dict[int, Card], awokenQueens : dict[int,Queen]):
        self.cards = cards
        self.awokenQueens = awokenQueens