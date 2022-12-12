from unittest import TestCase
from SleepingQueens.GameAdaptor import GameAdaptor

class TestGameAdaptor(TestCase):

    def discardFromHand(self, adaptor : GameAdaptor = GameAdaptor(['Jaro','Fifo','Kubo'])):

        a = [(adaptor.game.playersList[0].hand.getCards()[i].value,adaptor.game.playersList[0].hand.getCards()[i].type) for i in range(5)]
        adaptor.play('Jaro','h5')
        b = [(adaptor.game.playersList[0].hand.getCards()[i].value,adaptor.game.playersList[0].hand.getCards()[i].type) for i in range(5)]

        self.assertNotEqual(a, b)
