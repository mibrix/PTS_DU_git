from SleepingQueens.Position import HandPosition
from SleepingQueens.Position import AwokenQueenPosition
from SleepingQueens.Position import SleepingQueenPosition
from SleepingQueens.Game import Game
from SleepingQueens.GameObservable import GameObservable
from typing import Union


class GameAdaptor:


    def __init__(self, names : list[str]):
        self.players = names
        self.game = Game(len(names))
        self.gameObservable = GameObservable()
        for i in range(len(names)):
            self.gameObservable.addPlayer(i)
        self.gameObservable.add()

    def play(self, player : str , cards : str):
        idx_pl = self.players.index(player)
        temp = cards.split()
        to_play : list[Union[AwokenQueenPosition, SleepingQueenPosition, HandPosition]] = []
        for i in temp:
            if i[0] == 'h':
                to_play.append(HandPosition(int(i[1:])-1,idx_pl))
            elif i[0] == 'a':
                to_play.append(AwokenQueenPosition(int(i[2:])-1, int(i[1])-1))
            elif i[0] == 's':
                to_play.append(SleepingQueenPosition(int(i[1:])-1))

        #notifikuj dotknute observeri
        out = self.game.play(idx_pl,to_play)
        self.gameObservable.gameObserver[0].notify(out[0][0])
        self.gameObservable.playerObservers[out[1][0]].notify(out[0][0])
        if len(out[1]) == 2:
            self.gameObservable.playerObservers[out[1][1]].notify(out[0][0])
        if(len(out) > 2):
            self.gameObservable.notifyAll(out[0][0])

