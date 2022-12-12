from unittest import TestCase
from SleepingQueens.Game import Game
from SleepingQueens.dataStructures import HandPosition

class TestGame(TestCase):

    def gameStateHandEqualHandHand(self,game : Game = Game(3)):
        #test ci ma hrac na ruke 5 kariet a ci su rovnake s tymi v gamestate
        hand = []
        for i in game.playersList[0].hand.getCards():
            hand.append([i.value,i.type])

        state = []
        for i,y in game.gameState.cards.items():
            if i.getPlayerIndex() == 0:
                state.append([y.value,y.type])

        self.assertEqual(state, hand)

    def discardFromHand(self, game: Game = Game(3)):
        a =[(game.playersList[0].hand.getCards()[i].value,game.playersList[0].hand.getCards()[i].type) for i in range(5)]
        game.play(0,[HandPosition(0,0)])
        b = [(game.playersList[0].hand.getCards()[i].value,game.playersList[0].hand.getCards()[i].type) for i in range(5)]

        self.assertNotEqual(a, b)
