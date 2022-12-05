from SleepingQueens.Position import AwokenQueenPosition
from SleepingQueens.QueenCollection import AwokenQueens

class MoveQueen:

    def __init__(self,opponentQueens : AwokenQueens):
        self.opponentQueens = opponentQueens

    def play(self, targetQueen : AwokenQueenPosition, tragerPlayerIdx : int) -> bool:
        if targetQueen.getCardIndex() not in [i.getCardIndex() for i in self.opponentQueens.getQueens().keys()]:
            return False
        self.opponentQueens.removeQueen(targetQueen)
        return True