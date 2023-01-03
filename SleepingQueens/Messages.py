from typing import Union

class Messages:

    def DiscardMessage(self, who : int, how_many : int) -> list[list[Union[str,int]]]:
        temp = ['nula', 'jedna', 'dva', 'tri']
        return [[f'Hrac {who} uspesne vyhodil {temp[how_many]} kartu/y'],[who]]

    def UnsuccessfulTurnMessage(self, who : int):
        return [["Neuspeny tah. Tah zopakuj!"],[who],False]

    def SuccessfulAttackMessage(self, attacker : int, attacked : int):
        return [[f'Hrac {attacker} uspesne zautocil na kralovnu hraca {attacked}'], [attacker, attacked]]

    def UnsuccessfulAttackMessage(self, attacker : int, attacked : int):
        return [[f'Hrac {attacked} sa ubranil pred utokom hraca {attacker}'],[attacker,attacked]]

    def SuccussfullyAwokenMessage(self, who):
        return [[f'Hrac {who} uspesne zobudil kralovnu'],[who]]




