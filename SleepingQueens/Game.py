from SleepingQueens.Player import Player
from SleepingQueens.dataStructures import PlayerState
from SleepingQueens.Hand import Hand
from SleepingQueens.Position import HandPosition
from SleepingQueens.Position import AwokenQueenPosition
from SleepingQueens.Position import SleepingQueenPosition
from typing import Union
from SleepingQueens.QueenCollection import SleepingQueens
from SleepingQueens.dataStructures import CardType
from SleepingQueens.dataStructures import Card
from SleepingQueens.DrawingAndTrashPile import DrawingAndTrashPile
from SleepingQueens.dataStructures import Queen
from SleepingQueens.dataStructures import GameState
import random
from SleepingQueens.GameFinished import GameFinished



class Game:
    queens = [Queen(random.randint(1, 15)) for _ in range(12)]
    kings = [Card(CardType(2), random.randint(1, 15)) for _ in range(8)]
    knights = [Card(CardType(3), random.randint(1, 15)) for _ in range(4)]
    sleeping_potions = [Card(CardType(4), random.randint(1, 15)) for _ in range(4)]
    wands = [Card(CardType(6), random.randint(1, 15)) for _ in range(3)]
    dragons = [Card(CardType(5), random.randint(1, 15)) for _ in range(3)]
    numbers = 4 * [Card(CardType(1), y) for y in range(1, 11)]
    gameFinished = GameFinished()

    def __init__(self,  numberOfPlayers : int, ):

        temp_q : dict[Union[AwokenQueenPosition, SleepingQueenPosition], Queen] = {}
        for n,i in enumerate(self.queens):
            temp_q[SleepingQueenPosition(n)] = i

        self.sleepingQueens = SleepingQueens(temp_q,'sleep')

        to_be_given = self.kings + self.knights + self.sleeping_potions + self.wands + self.dragons + self.numbers
        player_cards_temp = {}
        for a in range(numberOfPlayers):
            for b in range(5):
                player_cards_temp[HandPosition(b,a)] = to_be_given.pop(random.randint(0,len(to_be_given)-1))

        self.drawingAndTrashPile = DrawingAndTrashPile(to_be_given, [])

        self.gameState = GameState(numberOfPlayers, 0, set(self.sleepingQueens.getQueens().keys()), player_cards_temp,
                                   {},[])

        self.playersList = []
        for c in range(numberOfPlayers):
            cards_for_player_state = {}
            for position,card in player_cards_temp.items():
                if position.getPlayerIndex() == c:
                    cards_for_player_state[position.getCardIndex()] = card
            PlayerState(cards_for_player_state,{})
            self.playersList.append(Player(c, PlayerState(cards_for_player_state, {}), self.sleepingQueens,
                                           Hand(c,cards_for_player_state,self.drawingAndTrashPile),self.gameState))

    def play(self,playerIdx : int, cards:list[Union[HandPosition, AwokenQueenPosition, SleepingQueenPosition]]) -> list:
        if playerIdx != self.gameState.onTurn:
            return [[f'Hrac {playerIdx} nie je na rade!'],[playerIdx]]
        for i in cards:
            if type(i) == AwokenQueenPosition:
                self.playersList[playerIdx].set_opp_queen(self.playersList[i.getPlayerIndex()].awokenQueens)
                self.playersList[playerIdx].set_opp_hand(self.playersList[i.getPlayerIndex()].hand)

        out = self.playersList[playerIdx].play(cards)
        if len(out) != 3:
            if playerIdx+1 < self.gameState.numberOfPlayers:
                self.gameState.onTurn = playerIdx + 1
            else:
                self.gameState.onTurn = 0

        #game finish
        temp_fin = self.gameFinished.eval(self.gameState)
        if temp_fin[0]:
            return [[f'Hrac {temp_fin[1]} vyhral!'],[1,1,1]]
        return out

    def updateGameStateCards(self, removeHandPos : list[HandPosition], addHandPos : list[Card]):

        for y in range(len(removeHandPos)):
            for i in self.gameState.cards.keys():
                if (i.getCardIndex() == removeHandPos[y].getCardIndex() and
                        i.getPlayerIndex() == removeHandPos[y].getPlayerIndex()):
                    self.gameState.cards[i] = addHandPos[y]
                    break

    def updateGameStateAfterAttack(self, awQueenPos : AwokenQueenPosition, new_owner : int):
        to_pop = AwokenQueenPosition(-1,-1)
        temp_q = Queen(-1)
        for i in self.gameState.awokenQueens.keys():
            if (i.getCardIndex() == awQueenPos.getCardIndex() and
                    i.getPlayerIndex() == awQueenPos.getPlayerIndex()):
                to_pop = i
                temp_q = self.gameState.awokenQueens[i]
                break

        #vymaz kralovnu z awokenQueens daneho hraca
        if to_pop.cardIndex != -1 and temp_q.points != -1:
            self.gameState.awokenQueens.pop(to_pop)
            to_pop.playerIndex = new_owner

            #ak hrac iba uspava kralovnu
            if new_owner == -1:
                q_idx = 0
                if self.gameState.sleepingQueens != set():
                    q_idx = max([i.cardIndex for i in self.gameState.sleepingQueens]) + 1
                self.gameState.sleepingQueens.add(SleepingQueenPosition(q_idx))

            #ak hrac utoci na kralovnu druheho hraca
            else:
                if self.gameState.awokenQueens == {}:
                    to_pop.cardIndex = max([i.cardIndex for i in self.gameState.awokenQueens.keys()])+1
                else:
                    to_pop.cardIndex = 0

                self.gameState.awokenQueens[to_pop] = temp_q






