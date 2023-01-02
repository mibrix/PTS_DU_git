from SleepingQueens.dataStructures import GameState

class GameFinished:
    def eval(self, gameState : GameState) -> list:

        temp : dict[int, list[int]] = {}
        for handpos,queen in gameState.awokenQueens.items():
            if handpos.getPlayerIndex() not in temp.keys():
                temp[handpos.getPlayerIndex()] = [queen.points]
            else:
                temp[handpos.getPlayerIndex()].append(queen.points)

        if gameState.numberOfPlayers in [2,3]:
            for player,queens in temp.items():
                if len(queens) == 5 or sum(queens) >= 50:
                    return [True,player]

        elif gameState.numberOfPlayers in [4,5]:
            for player,queens in temp.items():
                if len(queens) == 4 or sum(queens) >= 40:
                    return [True,player]

        if len(gameState.sleepingQueens) == 0:
            max_points = 0
            pl_idx = -1
            for player,queenn in temp.items():
                if sum(queenn) > max_points:
                    max_points = sum(queenn)
                    pl_idx = player
            return [True, pl_idx]

        return [False]