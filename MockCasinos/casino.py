from random import randint


class Casino(object):
    # 游戏类型
    SICBO = 1  # 赌大小
    ROULETTE = 2  # 轮盘赌
    BACCARAT = 3  # 百家乐

    def __init__(self, jackpot, chips=1000):
        self.__jackpot = jackpot  # 庄家奖池
        self.__chips = chips  # 初始筹码

    def guest(self, money):
        self.__money = money  # 闲家本金

    def __getbet(self, ratio_r, ratio_p):
        ranker, player = 0, 0
        while self.__chips > 10:
            ranker = ratio_r * self.__chips
            player = ratio_p * self.__chips
            if (self.__jackpot - ranker) < 0 or (self.__money - player) < 0:
                self.__chips = self.__chips // 2
                continue
            break
        return ranker, player

    def __sicbo(self):
        bet = ['小', '大']
        bet_r = randint(0, 1)
        bet_p = 1 - bet_r
        ranker, player = self.__getbet(1, 1)
        print('庄家{0:}押【{1:}】'.format(ranker, bet[bet_r]))
        print('闲家{0:}押【{1:}】'.format(player, bet[bet_p]))
        sic1, sic2, sic3 = randint(1, 6), randint(1, 6), randint(1, 6)
        result = sic1 + sic2 + sic3
        print('色子点数：{0:}+{1:}+{2:}={3:}'.format(sic1, sic2, sic3, result))
        if (result > 9 and bet_r == 1) or (result <= 9 and bet_r == 0):
            ranker, player = player, -player
        else:
            ranker, player = -ranker, ranker
            self.__chips = self.__chips * 2
        self.__jackpot += ranker
        self.__money += player
        print('庄家收支：{0:} 闲家收支：{1:}'.format(ranker, player))

    def __roulette(self):
        bet = list(range(1, 9))
        bet_r = sorted([bet.pop(randint(0, len(bet) - 1)) for i in range(randint(1, 7))])
        bet_p = sorted(bet)
        ranker, player = self.__getbet(len(bet_r), len(bet_p))
        print('庄家{0:}押{1:}'.format(ranker, bet_r))
        print('闲家{0:}押{1:}'.format(player, bet_p))
        result = randint(1, 8)
        print('打珠落在[{0:}]号位置'.format(result))
        if result in bet_r:
            ranker, player = player, -player
        else:
            ranker, player = -ranker, ranker
            self.__chips = self.__chips * 2
        self.__jackpot += ranker
        self.__money += player
        print('庄家收支：{0:} 闲家收支：{1:}'.format(ranker, player))

    def __baccarat(self):
        bet = [1, 2, 3, 4, 5, 6, 7, 8, 9, '10', 'J', 'Q', 'K']
        while True:
            bet_r = [bet[randint(0, len(bet) - 1)] for i in range(3)]
            bet_p = [bet[randint(0, len(bet) - 1)] for i in range(3)]
            sum_r = sum(filter(lambda x: isinstance(x, int) == True, bet_r))
            sum_p = sum(filter(lambda x: isinstance(x, int) == True, bet_p))
            if (sum_r % 10) != (sum_p % 10):
                bet_r, bet_p = list(map(str, bet_r)), list(map(str, bet_p))
                break
        ranker, player = self.__getbet(1, 1)
        print('庄家{0:}押{1:}'.format(ranker, bet_r))
        print('闲家{0:}押{1:}'.format(player, bet_p))
        print('花色牌值：{0:}={1:} VS {2:}={3:}'.format('+'.join(bet_r), sum_r, '+'.join(bet_p), sum_p))
        if (sum_r % 10) > (sum_p % 10):
            ranker, player = player, -player
        else:
            ranker, player = -ranker, ranker
            self.__chips = self.__chips * 2
        self.__jackpot += ranker
        self.__money += player
        print('庄家收支：{0:} 闲家收支：{1:}'.format(ranker, player))

    def __game(self, number, game_type):
        if game_type == 0:
            types = (self.SICBO, self.ROULETTE, self.BACCARAT)
            game_type = types[randint(0, len(types) - 1)]
        numstr = '第' + str(number) + '局：'
        if game_type == self.SICBO:
            print('{0:*^40}'.format(numstr + '赌大小'))
            self.__sicbo()
        if game_type == self.ROULETTE:
            print('{0:*^40}'.format(numstr + '轮盘赌'))
            self.__roulette()
        if game_type == self.BACCARAT:
            print('{0:*^40}'.format(numstr + '百家乐'))
            self.__baccarat()
        print('庄家剩余：{0:} 闲家剩余：{1:}'.format(self.__jackpot, self.__money))

    def start(self, game_type=0, end_times=0, end_profit=0.0):
        number = 1  # 初始化对局数
        expect = self.__money * (1 + end_profit)
        while self.__jackpot > 0 and self.__money > 0:
            self.__game(number, game_type)
            if end_times != 0 and number > end_times:
                break
            if end_profit != 0.0 and self.__money >= expect:
                break
            number += 1
