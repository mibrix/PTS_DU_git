from SleepingQueens.dataStructures import PlayerState
from SleepingQueens.Hand import Hand
from SleepingQueens.EvaluateNumberedCards import EvaluateNumberedCards
from SleepingQueens.Position import HandPosition
from SleepingQueens.Position import AwokenQueenPosition
from SleepingQueens.Position import SleepingQueenPosition
from typing import Union
from SleepingQueens.QueenCollection import AwokenQueens
from SleepingQueens.QueenCollection import SleepingQueens
from SleepingQueens.dataStructures import CardType
from SleepingQueens.EvaluateAttack import EvaluateAttack
from SleepingQueens.MoveQueen import MoveQueen
from SleepingQueens.dataStructures import GameState



class Player():

    def __init__(self, playerIdx : int, playerState : PlayerState, currentlySleepingQueens : SleepingQueens,
                 hand : Hand, gameState : GameState):
        self.playerState = playerState
        self.hand = hand
        self.playerIdx = playerIdx
        self.evaluateNumberedCards = EvaluateNumberedCards()
        self.awokenQueens = AwokenQueens({},'awake',playerIdx)
        self.currentTargetOpponentHand : Hand
        self.currentTargetOpponentQueens : AwokenQueens
        self.currentlySleepingQueens = currentlySleepingQueens
        self.gameState = gameState


    def play(self, cards : list[Union[HandPosition, AwokenQueenPosition, SleepingQueenPosition]]) -> list:

        #ak hrac iba vyhadzuje jednu kartu
        if len(cards) == 1:
            self.hand.pickCards(cards)
            new_card = self.hand.removePickedCardsAndRedraw()[0]
            self.playerState.cards[cards[0].getCardIndex()] = new_card

            #updatuj gameState
            for i in self.gameState.cards.keys():
                if (i.getCardIndex() == cards[0].getCardIndex() and
                    i.getPlayerIndex() == self.playerIdx):
                    self.gameState.cards[i] = new_card
                    break

            return [[f'Hrac {self.playerIdx} uspesne vyhodil kartu'],[self.playerIdx]]


        #pripad kedy chce hrac zahrat komplexny tah
        elif len(cards) == 2:
            #hrac chce vyhodit dve ciselne karty
            if (self.playerState.cards[cards[0].getCardIndex()].type == CardType.Number
                and self.playerState.cards[cards[1].getCardIndex()].type == CardType.Number):
                if self.evaluateNumberedCards.play([self.playerState.cards[i.getCardIndex()] for i in cards]):
                    self.hand.pickCards(cards)
                    new_cards = self.hand.removePickedCardsAndRedraw()
                    for i in range(2):
                        self.playerState.cards[cards[i].getCardIndex()] = new_cards[i]

                    #updatuj gamestate
                    for y in range(2):
                        for i in self.gameState.cards.keys():
                            if (i.getCardIndex() == cards[y].getCardIndex() and
                                    i.getPlayerIndex() == self.playerIdx):
                                self.gameState.cards[i] = new_cards[y]
                                break

                    return [[f'Hrac {self.playerIdx} uspesne vyhodil dve karty'],[self.playerIdx]]
                #poslal dve karty z rozdielnym cislom
                else:
                    return [["Neuspeny tah. Tah zopakuj!"],[self.playerIdx],False]

            #hrac chce zobrat kralovnu superovi
            elif((self.playerState.cards[cards[0].getCardIndex()].type == CardType.Knight
                and cards[1].getPlayerIndex() != self.playerIdx)
            or   (self.playerState.cards[cards[1].getCardIndex()].type == CardType.Knight
                and cards[0].getPlayerIndex() != self.playerIdx)):

                    temp = EvaluateAttack(CardType.Dragon, self.currentTargetOpponentHand ,self.currentTargetOpponentQueens)
                    if cards[0].getPlayerIndex() != self.playerIdx:
                        opp_ind = cards[0].getPlayerIndex()
                        ind = 0
                    else:
                        opp_ind = cards[1].getPlayerIndex()
                        ind = 1
                    #hrac sa ubranil
                    if temp.play(cards[ind],cards[ind].getPlayerIndex()):
                        return [[f'Hrac {cards[ind].getPlayerIndex()} sa ubranil pred utokom hraca {self.playerIdx}'],
                                [cards[ind].getPlayerIndex(),self.playerIdx]]
                    # presun kralovnu
                    else:
                        temp = MoveQueen(self.currentTargetOpponentQueens)
                        temp_q = ''
                        #ak uspesne vymaze opponentovy pripise sebe
                        for i in self.currentTargetOpponentQueens.getQueens().keys():
                            if cards[ind].getCardIndex() == i.getCardIndex():
                                temp_q = self.currentTargetOpponentQueens.getQueens()[i]
                                break

                        if temp_q == '':
                            return [[f'Hrac {cards[ind].getPlayerIndex()} nema danu kralovnu'],[self.playerIdx], False]

                        if temp.play(cards[ind], cards[ind].getPlayerIndex()):
                            self.awokenQueens.addQueen(temp_q)
                            if self.playerState.awokenQueens != {}:
                                self.playerState.awokenQueens[max([i for i in self.playerState.awokenQueens.keys()])+1] = temp_q
                                #update gamestate
                                to_pop = ''
                                for i in self.gameState.awokenQueens.keys():
                                    if (i.getCardIndex() == cards[ind].getCardIndex() and
                                            i.getPlayerIndex() == opp_ind):
                                        to_pop = i
                                        break
                                self.gameState.awokenQueens[AwokenQueenPosition(
                                   max([i for i in self.playerState.awokenQueens.keys()])+1,self.playerIdx)] = temp_q
                                if to_pop != '':
                                    self.gameState.awokenQueens.pop(to_pop)

                            else:
                                self.playerState.awokenQueens[0] = temp_q
                                #update gamestate
                                to_pop = ''
                                for i in self.gameState.awokenQueens.keys():
                                    if (i.getCardIndex() == cards[ind].getCardIndex() and
                                            i.getPlayerIndex() == opp_ind):
                                        to_pop = i
                                        break
                                self.gameState.awokenQueens[AwokenQueenPosition(0,self.playerIdx)]= temp_q
                                if to_pop != '':
                                    self.gameState.awokenQueens.pop(to_pop)
                            return [[f'Hrac {self.playerIdx} uspesne zautocil na kralovnu hraca {cards[ind].getPlayerIndex()}'],
                                    [cards[ind].getPlayerIndex(),self.playerIdx]]

            # #hrac chce uspat kralovnu superovi
            elif ((self.playerState.cards[cards[0].getCardIndex()].type == CardType.SleepingPotion
                   and cards[1].getPlayerIndex() != self.playerIdx)
                  or (self.playerState.cards[cards[1].getCardIndex()].type == CardType.SleepingPotion
                      and cards[0].getPlayerIndex() != self.playerIdx)):

                temp = EvaluateAttack(CardType.MagicWand, self.currentTargetOpponentHand, self.currentTargetOpponentQueens)
                if cards[0].getPlayerIndex() != self.playerIdx:
                    opp_ind = cards[0].getPlayerIndex()
                    ind = 0
                else:
                    opp_ind = cards[1].getPlayerIndex()
                    ind = 1
                # hrac sa ubranil
                if temp.play(cards[ind], cards[ind].getPlayerIndex()):
                    return [[f'Hrac {cards[ind].getPlayerIndex()} sa ubranil pred utokom hraca {self.playerIdx}'],
                            [self.playerIdx,cards[ind].getPlayerIndex()]]
                # presun kralovnu
                else:
                    temp = MoveQueen(self.currentTargetOpponentQueens)
                    temp_q = ''
                    # ak uspesne vymaze opponentovy prida na flop
                    for i in self.currentTargetOpponentQueens.getQueens().keys():
                        if cards[ind].getCardIndex() == i.getCardIndex():
                            temp_q = self.currentTargetOpponentQueens.getQueens()[i]
                            break

                    if temp_q == '':
                        return [[f'Hrac {cards[ind].getPlayerIndex()} nema danu kralovnu'],[self.playerIdx],False]

                    if temp.play(cards[ind], cards[ind].getPlayerIndex()):
                        self.currentlySleepingQueens.addQueen(temp_q)

                        # update gamestate
                        to_pop = ''
                        for i in self.gameState.awokenQueens.keys():
                            if (i.getCardIndex() == cards[ind].getCardIndex() and
                                    i.getPlayerIndex() == opp_ind):
                                to_pop = i
                                break

                        if to_pop != '':
                            self.gameState.awokenQueens.pop(to_pop)

                        return [[f'Hrac {self.playerIdx} uspesne zautocil na kralovnu hraca {cards[ind].getPlayerIndex()}']
                                ,[self.playerIdx,cards[ind].getPlayerIndex()]]


            # hrac chce zobudit kralovnu
            elif ((self.playerState.cards[cards[0].getCardIndex()].type == CardType.King
                   and type(cards[1]) == SleepingQueenPosition )
                  or (self.playerState.cards[cards[1].getCardIndex()].type == CardType.King
                      and type(cards[0]) == SleepingQueenPosition)):
                if cards[0].getPlayerIndex() != self.playerIdx:
                    ind = 0
                else:
                    ind = 1

                temp_q = self.currentlySleepingQueens.removeQueen(cards[ind])
                q_ind = self.awokenQueens.addQueen(temp_q)

                # update gamestate
                self.gameState.awokenQueens[AwokenQueenPosition(q_ind,self.playerIdx)] = temp_q

                return [[f'Hrac {self.playerIdx} uspesne zobudil kralovnu'],[self.playerIdx]]

        elif len(cards) == 3:
            if (self.playerState.cards[cards[0].getCardIndex()].type == CardType.Number
                    and self.playerState.cards[cards[1].getCardIndex()].type == CardType.Number
                    and self.playerState.cards[cards[2].getCardIndex()].type == CardType.Number):
                if self.evaluateNumberedCards.play([self.playerState.cards[i.getCardIndex()] for i in cards]):
                    self.hand.pickCards(cards)
                    new_cards = self.hand.removePickedCardsAndRedraw()
                    for i in range(3):
                        self.playerState.cards[cards[i].getCardIndex()] = new_cards[i]
                    return [[f'Hrac {self.playerIdx} vyhodil 3 karty'],[self.playerIdx]]
                else:
                    return [[f'Hrac {self.playerIdx} sa neuspesne pokusil vyhodit 3 karty. Zopakuj tah!'],[self.playerIdx],
                            False]
        return [[f'Hrac {self.playerIdx} sa neuspesne pokusil vyhodit 0 alebo viac ako 3 karty. Zopakuj tah!'],
                [self.playerIdx], False]

    def set_opp_queen(self, opp_queens : AwokenQueens):
        self.currentTargetOpponentQueens = opp_queens

    def set_opp_hand(self, opp_hand : Hand):
        self.currentTargetOpponentHand = opp_hand

