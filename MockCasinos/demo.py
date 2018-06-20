try:
    exec('from casino import Casino')
except:
    from .casino import Casino

if __name__ == '__main__':
    jackpot = 10000 * 10000  # 庄家初始资金
    money = 100 * 10000  # 闲家初始资金
    casino = Casino(jackpot)
    casino.guest(money)
    casino.start(end_times=0, end_profit=0.0)
