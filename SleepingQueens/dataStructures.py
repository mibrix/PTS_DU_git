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

class PlayerState:
    def __init__(self, cards : dict[int, Card], awokenQueens : dict[int,Queen]):
        self.cards = cards
        self.awokenQueens = awokenQueens