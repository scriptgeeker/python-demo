'''
Gambling probability statistics
'''
from random import randint


class Casino(object):

    def __init__(self, chip=100):
        self.__chip = chip
        self.__record = []

    def __del__(self):
        count = len(self.__record)
        wins = sum([i[2] for i in self.__record])
        rate = (wins / count) * 100
        print('Count:{:} Wins:{:} Rate:{:.2f}%'.format(count, wins, rate))

    def ranker(self, jackpot):
        self.jackpot = jackpot

    def player(self, money):
        self.money = money

    def game(self, index, stake):
        info = [index, stake]
        if randint(0, 1) == 0:
            info.append(True)
            self.jackpot -= stake
            self.money += stake
        else:
            info.append(False)
            self.jackpot += stake
            self.money -= stake
        info.extend([self.jackpot, self.money])
        return info

    def start(self, times=0, profit=0.0):
        income = self.money * (1 + profit)
        index, stake = 0, self.__chip
        while not (self.jackpot < self.__chip or self.money < self.__chip):
            if (times != 0 and index >= times) or profit != 0.0:
                if self.money >= income:
                    return 1  # player win
                elif profit == 0.0:
                    return 0  # ranker win
            self.__record.append(self.game(index, stake))
            # adjust stake money
            stake = stake * 2  # chip double
            while stake > self.jackpot or stake > self.money:
                stake = stake // 2
            index = index + 1

        if self.jackpot > self.money:
            return 0  # ranker win
        else:
            return 1  # player win


if __name__ == '__main__':
    param = {
        'count': 10000,
        'chip': 100,
        'jackpot': 10000 * 10000,
        'money': 100 * 10000,
        'times': 0,
        'profit': 0.7,
    }
    record = []
    for i in range(param['count']):
        casino = Casino(param['chip'])  # 初始筹码
        casino.ranker(param['jackpot'])
        casino.player(param['money'])
        result = casino.start(param['times'], param['profit'])
        record.append(result)
        del casino
    param['possible'] = '{:.2f}%'.format((sum(record) / len(record)) * 100)

    with open('record.log', 'a', encoding='utf8') as fa:
        paramstr = [
            '样本数量：{count}',
            '筹码单位：{chip}',
            '庄家本金：{jackpot}',
            '闲家本金：{money}',
            '次数限制：{times}',
            '利率限制：{profit}',
            '获胜概率：{possible}',
        ]
        fa.write(('\t'.join(paramstr) + '\n').format(**param))

    print(param)
