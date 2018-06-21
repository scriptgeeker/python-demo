## 模拟赌场

既然赌博每局的胜率为50%，为何最终有那么多人会赌到倾家荡产？

----------
### 知乎提问
假设赌博输赢的概率都是50％，那么长期赌博的人为什么仍然会更容易倾家荡产而不是收益均衡？

### 赌场规则

 1. 通过在小游戏上押注，开始一句游戏
 2. 一局游戏只有两种结果，赢或输（平局加赛一局）
 3. 赢的一方收回自己的筹码并获取对方全部筹码
 4. 庄家输了，则下局筹码加倍

### 游戏介绍

 1. 赌大小：押大或押小，三个色子点数总和大于9则押大一方胜
 2. 轮盘赌：从8个数中押号码，打珠后珠子落点的数字就是得奖号码
 3. 百家乐：抽3张牌，总和的最后一位为9或接近9则胜利（10 J Q K 按0算）

### 结束条件

 1. 盈利比例：闲家获得本金一定比例的利润后结束
 2. 游戏次数：指定进行到多少局时游戏结束
 3. 强制结束：庄家或闲家手里的筹码输光，则游戏结束

### 文件索引

 - [casino.py][1]（模拟赌场类 - Analog Casinos）
 - [demo.py][2]（进行游戏博弈 - Start a mock Casino）
 - [gamble.py][3]（计算获胜概率 - Calculation probability）

### 参考链接
[【七月在线实验室】一夜暴富还是倾家荡产？Python模拟赌博实验][4]


**最后啰嗦一句: 珍惜生命,远离赌博**


  [1]: https://github.com/scriptgeeker/python-demo/blob/master/MockCasinos/casino.py
  [2]: https://github.com/scriptgeeker/python-demo/blob/master/MockCasinos/demo.py
  [3]: https://github.com/scriptgeeker/python-demo/blob/master/MockCasinos/gamble.py
  [4]: https://blog.csdn.net/T7SFOKzorD1JAYMSFk4/article/details/79989949