from SleepingQueens.dataStructures import Queen
from SleepingQueens.Position import SleepingQueenPosition
from SleepingQueens.Position import AwokenQueenPosition
from typing import Union

class QueenCollection:
    def __init__(self, QueensList : dict[Union[AwokenQueenPosition, SleepingQueenPosition], Queen], typ:str,
                 playerIdx : int = -1) :
        self.QueensList = QueensList
        self.playerIdx = playerIdx
        self.typ = typ

    def addQueen(self, queen: Queen) -> int:
        #add queen to the first empty position
        if self.QueensList == {}:
            if self.typ == 'awake':
                self.QueensList[AwokenQueenPosition(0,self.playerIdx)] = queen
            elif self.typ == 'sleep':
                self.QueensList[SleepingQueenPosition(0)] = queen
            return 0
        else:
            temp = [i.getCardIndex() for i in self.QueensList.keys()]
            temp.sort()
            if self.typ == 'awake':
                self.QueensList[AwokenQueenPosition(temp[-1]+1,self.playerIdx)] = queen
            elif self.typ == 'sleep':
                self.QueensList[SleepingQueenPosition(temp[-1]+1)] = queen
            return temp[-1]+1

    def removeQueen(self,position : Union[AwokenQueenPosition, SleepingQueenPosition]) -> Queen:
        for i in self.getQueens().keys():
            if position.getCardIndex() == i.getCardIndex():
                temp = self.QueensList[i]
                self.QueensList.pop(i)
                return temp


    def getQueens(self) -> dict[Union[AwokenQueenPosition, SleepingQueenPosition], Queen]:
        return self.QueensList


class SleepingQueens(QueenCollection):
    def __init__(self, QueensList : dict[Union[AwokenQueenPosition, SleepingQueenPosition], Queen], typ:str):
        super().__init__(QueensList, typ)


class AwokenQueens(QueenCollection):
    def __init__(self, QueensList : dict[Union[AwokenQueenPosition, SleepingQueenPosition], Queen],typ:str, playerIdx : int = -1):
        super().__init__(QueensList, typ, playerIdx)