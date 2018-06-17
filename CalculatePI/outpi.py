import time
import threading


# 执行时间装饰器
def exetime(func):
    def inner(*args, **kwargs):
        ts = time.time()
        res = func(*args, **kwargs)
        te = time.time()
        print('Execution time {0:.3f}s'.format(te - ts))
        return res

    return inner


# 计算圆周率
def getpi(num):
    global i
    b = 10 ** (num + 10)
    x1 = 16 * b // 5
    x2 = -4 * b // 239
    pi = x1 + x2
    for i in range(3, num * 2, 2):
        x1 //= -5 ** 2
        x2 //= -239 ** 2
        pi += (x1 + x2) // i
    pi, i = str(pi), 0.0
    return pi[0] + '.' + pi[1:-10]


# 打印计算进度
def conlog(num):
    global i
    while isinstance(i, int):
        now = time.localtime(time.time())
        print(num * 2 - i, time.strftime('%H:%M:%S', now))
        # 每隔3秒打印一次
        time.sleep(3)


@exetime
def savepi(num, file):
    pi = getpi(num)
    with open(file, 'w') as fw:
        fw.write(pi)


if __name__ == '__main__':
    i = 0  # 全局变量
    num = 10 ** 6  # 计算精度100万位
    file = 'pi.txt'  # 计算结果保存到文件
    ts = threading.Thread(target=savepi, args=(num, file))
    tc = threading.Thread(target=conlog, args=(num,))
    ts.start()  # 多线程S用于计算圆周率
    tc.start()  # 多线程C用于查询进度
    ts.join()
    tc.join()
