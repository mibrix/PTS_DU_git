import Player
from Player import Player
from dataStructures import PlayerState
from Hand import Hand
from Position import HandPosition
from Position import AwokenQueenPosition
from Position import SleepingQueenPosition
from typing import Union
from QueenCollection import SleepingQueens
from dataStructures import CardType
from dataStructures import Card
from DrawingAndTrashPile import DrawingAndTrashPile
from dataStructures import Queen
from dataStructures import GameState
import random
from GameFinished import GameFinished



class Game:
    queens = [Queen(random.randint(1, 15)) for i in range(12)]
    kings = [Card(CardType(2), random.randint(1, 15)) for y in range(8)]
    knights = [Card(CardType(3), random.randint(1, 15)) for y in range(4)]
    sleeping_potions = [Card(CardType(4), random.randint(1, 15)) for y in range(4)]
    wands = [Card(CardType(6), random.randint(1, 15)) for y in range(3)]
    dragons = [Card(CardType(5), random.randint(1, 15)) for y in range(3)]
    numbers = 4 * [Card(CardType(1), y) for y in range(1, 11)]
    gameFinished = GameFinished()

    def __init__(self,  numberOfPlayers : int, ):

        temp_q = {}
        for n,i in enumerate(self.queens):
            temp_q[SleepingQueenPosition(n)] = i

        self.sleepingQueens = SleepingQueens(temp_q,'sleep')

        to_be_given = self.kings + self.knights + self.sleeping_potions + self.wands + self.dragons + self.numbers
        player_cards_temp = {}
        for i in range(numberOfPlayers):
            for y in range(5):
                player_cards_temp[HandPosition(y,i)] = to_be_given.pop(random.randint(0,len(to_be_given)-1))

        self.drawingAndTrashPile = DrawingAndTrashPile(to_be_given, [])

        self.gameState = GameState(numberOfPlayers, 0, set(self.sleepingQueens.getQueens().keys()), player_cards_temp,
                                   {},[])

        self.playersList = []
        for i in range(numberOfPlayers):
            cards_for_player_state = {}
            for position,card in player_cards_temp.items():
                if position.getPlayerIndex() == i:
                    cards_for_player_state[position.getCardIndex()] = card
            PlayerState(cards_for_player_state,{})
            self.playersList.append(Player(i, PlayerState(cards_for_player_state, {}), self.sleepingQueens,
                                           Hand(i,cards_for_player_state,self.drawingAndTrashPile)))

    def play(self,playerIdx : int, cards:list[Union[HandPosition, AwokenQueenPosition, SleepingQueenPosition]]) -> list:
        if playerIdx != self.gameState.onTurn:
            return [[f'Hrac {playerIdx} nie je na rade!'],[playerIdx]]
        for i in cards:
            if type(i) == AwokenQueenPosition:
                self.playersList[playerIdx].set_opp_queen(self.playersList[i.getPlayerIndex()].awokenQueens)
                self.playersList[playerIdx].set_opp_hand(self.playersList[i.getPlayerIndex()].hand)

        out = self.playersList[playerIdx].play(cards)
        if len(out) != 3:
            if playerIdx < self.gameState.numberOfPlayers:
                self.gameState.onTurn = playerIdx + 1
            else:
                self.gameState.onTurn = 0

        #game finish
        temp_fin = self.gameFinished.eval(self.gameState)[0]
        if temp_fin[0]:
            return [[f'Hrac {temp_fin[1]} vyhral!'],[1,1,1]]
        return out

#test ci ma hrac na ruke 5 kariet a ci su rovnake s tymi v gamestate
# a = Game(3)
# print(a.playersList[0].hand.getCards())
# for i in a.playersList[0].hand.getCards():
#     print(i.value,i.type)
#
# print()
# for i,y in a.gameState.cards.items():
#     if i.getPlayerIndex() == 0:
#         print(y.value,y.type)

#napisat test na utok

# a = Game(3)
# print([(a.playersList[0].hand.getCards()[i].value,a.playersList[0].hand.getCards()[i].type) for i in range(5)])
# a.play(0,[HandPosition(0,0)])
# print([(a.playersList[0].hand.getCards()[i].value,a.playersList[0].hand.getCards()[i].type) for i in range(5)])

#ak je karta HandPosition(0,0) kral
#a.play(0,[HandPosition(0,0),SleepingQueenPosition(0)])
#len(a.sleepingQueens.getQueens())
#a.playersList[0].awokenQueens.getQueens()

#ak ma hrac0 kralovnu a HandPosition(0,1) je knight
# a.play(1,[HandPosition(0,1),AwokenQueenPosition(0,0)])
# a.playersList[0].awokenQueens.getQueens()
# a.playersList[1].awokenQueens.getQueens()

