from SleepingQueens.dataStructures import Card
from SleepingQueens.dataStructures import CardType

class EvaluateNumberedCards:

    def play(self, cards : list[Card]) -> bool:
        if len(cards) == 2:
            if cards[0].type == CardType.Number and cards[1].type == CardType.Number:
                if cards[0].value == cards[1].value:
                    return True
            return False

        if len(cards) == 3:
            if cards[0].type == CardType.Number and cards[1].type == CardType.Number and cards[2].type == CardType.Number:
                print(cards[0].value,cards[1].value,cards[2].value)
                if cards[0].value + cards[1].value == cards[2].value:
                    return True
                elif cards[1].value + cards[2].value == cards[0].value:
                    return True
                elif cards[0].value + cards[2].value == cards[1].value:
                    return True
            return False
        return False