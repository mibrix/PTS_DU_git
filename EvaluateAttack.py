from dataStructures import CardType
from Position import AwokenQueenPosition
from Hand import Hand
from QueenCollection import AwokenQueens

class EvaluateAttack:

    def __init__(self, defenseCardType : CardType, opponentHand : Hand, opponentQueens : AwokenQueens):
        self.defenseCardType = defenseCardType
        self.opponentHand = opponentHand
        self.opponentQueens = opponentQueens

    def play(self, targetQueen : AwokenQueenPosition, tragerPlayerIdx : int) -> bool:
        if self.opponentHand.hasCardOfType(self.defenseCardType).getCardIndex() != -1:
                return True
        return False