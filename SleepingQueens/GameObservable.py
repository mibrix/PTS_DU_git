
class GameObserver:
    def __init__(self):
        self.messages : list[str] = []

    def notify(self,message : str):
        self.messages.append(message)
        return message


class GameObservable:

    def __init__(self):
        self.gameObserver : list[GameObserver] = []
        self.playerObservers : dict[int : GameObserver] = {}

    def add(self, observer : GameObserver = GameObserver()):
        self.gameObserver.append(observer)

    def addPlayer(self, playerIdx : int, observer : GameObserver = GameObserver()):
        self.playerObservers[playerIdx] = observer

    def remove(self, playerIdx : int):
        if playerIdx == -1:
            self.gameObserver = []
        else:
            self.playerObservers.pop(playerIdx)

    def notifyAll(self, message : str):
        for i in self.gameObserver:
            i.notify(message)

        for i in self.playerObservers:
            i.notify(message)

