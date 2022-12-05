from unittest import TestCase
from SleepingQueens.dataStructures import PlayerState
from SleepingQueens.Player import Player
from SleepingQueens.QueenCollection import SleepingQueens
from SleepingQueens.Hand import Hand
from SleepingQueens.DrawingAndTrashPile import DrawingAndTrashPile
from SleepingQueens.dataStructures import GameState

class TestPlayer(TestCase):

    def index(self, indexPl : int):
        a = Player(indexPl, PlayerState({},{}),SleepingQueens({},'sleep'), Hand(1,{},DrawingAndTrashPile([],[])),
                   GameState(3,1,set(),{},{},[]))
        self.assertEqual(a.playerIdx, indexPl)

    def playerState(self):
        a = Player(0, PlayerState({},{}),SleepingQueens({},'sleep'), Hand(1,{},DrawingAndTrashPile([],[])),
                   GameState(3,1,set(),{},{},[]))
        self.assertEqual(a.playerState.cards,{})
        self.assertEqual(a.playerState.awokenQueens, {})
