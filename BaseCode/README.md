## 字节码编码

模拟从二进制到字符的编码过程，封装Base64编解码工具

----------

### 核心原理

Base64是一种用64个字符来表示任意二进制数据的方法。

![Base64字母映射表][1]

Base64编码会把3字节的二进制数据编码为4字节的文本数据。
![字节数据转换过程][2]


### 文件索引

 - [demo.py][3]（内建模块的使用 - Use of built-in modules）

### 参考博客
[【廖雪峰的官方网站】Python内建模块 Base64][4]

[【CSDN viclee108】关于Base64编码的理解][5]

[【博客园 luguo3000】从原理上搞定Base64编码][6]


  [1]: https://raw.githubusercontent.com/scriptgeeker/python-demo/master/__CDN__/Base64-alphabet.png
  [2]: https://raw.githubusercontent.com/scriptgeeker/python-demo/master/__CDN__/Base64-principle.png
  [3]: https://github.com/scriptgeeker/python-demo/blob/master/BaseCode/demo.py
  [4]: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000
  [5]: https://blog.csdn.net/goodlixueyong/article/details/52132250
  [6]: http://www.cnblogs.com/luguo3000/p/3940197.html