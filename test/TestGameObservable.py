from SleepingQueens.GameAdaptor import GameAdaptor
from SleepingQueens.dataStructures import Card
from SleepingQueens.dataStructures import CardType
from unittest import TestCase


class TestGameObservabale(TestCase):
    def zahodJednuKartu(self, gameA: GameAdaptor):
        gameA.play('Jano', 'h1')
        self.assertEqual(gameA.gameObservable.playerObservers[0].messages, ['Hrac 0 uspesne vyhodil kartu'])

    def zobudKralovnu(self, gameA: GameAdaptor):
        gameA.game.playersList[0].hand.currentHand[5] = Card(CardType.King, 5)
        gameA.play('Jano', 'h6 s1')
        self.assertEqual(gameA.gameObservable.playerObservers[0].messages, ['Hrac 0 uspesne zobudil kralovnu'])


    def zoberKralovnuOponentovi(self, gameA: GameAdaptor):
        gameA.play('Jano', 'h2')
        gameA.game.playersList[1].hand.currentHand[5] = Card(CardType.King, 5)
        gameA.play('Fero', 'h6 s1')
        gameA.play('Juro', 'h1')
        gameA.game.playersList[0].hand.currentHand[5] = Card(CardType.Knight, 5)
        gameA.play('Jano', 'h6 a21')
        self.assertEqual(gameA.gameObservable.gameObserver[0].messages
                         , ['Hrac 0 uspesne vyhodil kartu', 'Hrac 1 uspesne zobudil kralovnu'
                             , 'Hrac 2 uspesne vyhodil kartu', 'Hrac 1 sa ubranil pred utokom hraca 0'])


    def vyhodDveKarty(self, gameA: GameAdaptor):
        gameA.game.playersList[0].hand.currentHand[0] = Card(CardType.Number, 3)
        gameA.game.playersList[0].hand.currentHand[1] = Card(CardType.Number, 3)
        gameA.play('Jano', 'h1 h2')
        self.assertEqual(gameA.gameObservable.gameObserver[0].messages, ['Hrac 0 uspesne vyhodil dve karty'])

    def vyhodTriKarty(self, gameA : GameAdaptor):
        gameA.game.playersList[0].hand.currentHand[0] = Card(CardType.Number,3)
        gameA.game.playersList[0].hand.currentHand[1] = Card(CardType.Number,3)
        gameA.game.playersList[0].hand.currentHand[2] = Card(CardType.Number,6)
        gameA.play('Jano','h1 h2 h3')
        self.assertEqual(gameA.gameObservable.gameObserver[0].messages, ['Hrac 0 vyhodil 3 karty'])

    def uspiKralovnu(self, gameA : GameAdaptor):
        gameA.play('Jano', 'h2')
        gameA.game.playersList[1].hand.currentHand[5] = Card(CardType.King, 5)
        gameA.play('Fero', 'h6 s1')
        gameA.play('Juro', 'h1')
        gameA.game.playersList[0].hand.currentHand[5] = Card(CardType.SleepingPotion, 5)
        gameA.play('Jano', 'h6 a21')
        self.assertEqual(gameA.gameObservable.gameObserver[0].messages,['Hrac 0 uspesne vyhodil kartu',
                                                                        'Hrac 1 uspesne zobudil kralovnu',
                                                         'Hrac 2 uspesne vyhodil kartu',
                                                         'Hrac 0 uspesne zautocil na kralovnu hraca 1'])

    def koniecHry(self, gameA : GameAdaptor):
        for i in range(5):
            gameA.game.playersList[0].hand.currentHand[5] = Card(CardType.King,5)
            gameA.play('Jano',f'h6 s{i+1}')
            if gameA.gameObservable.gameObserver[0].messages[-1] == 'Hrac 0 vyhral!':
                break
            gameA.play('Fero','h1')
            gameA.play('Juro','h1')
        self.assertEqual(gameA.gameObservable.gameObserver[0].messages,['Hrac 0 uspesne zobudil kralovnu',
                                                                        'Hrac 1 uspesne vyhodil kartu',
                                                                        'Hrac 2 uspesne vyhodil kartu',
                                                                        'Hrac 0 uspesne zobudil kralovnu',
                                                                        'Hrac 1 uspesne vyhodil kartu',
                                                                        'Hrac 2 uspesne vyhodil kartu',
                                                                        'Hrac 0 uspesne zobudil kralovnu',
                                                                        'Hrac 1 uspesne vyhodil kartu',
                                                                        'Hrac 2 uspesne vyhodil kartu',
                                                                        'Hrac 0 vyhral!'])

