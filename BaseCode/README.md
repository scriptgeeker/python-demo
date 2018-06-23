## 字节码编码

模拟从二进制到字符的编码过程，封装Base64编解码工具

----------

### 核心原理

Base64是一种用64个字符来表示任意二进制数据的方法。
![字节数据转换过程][1]
Base64编码会把3字节的二进制数据编码为4字节的文本数据。

### 文件索引

 - [demo1.py][2]（内建模块的使用 - Use of built-in modules）
 - [mybase.py][3]（编码过程的实现 - Coding implementation）
 - [base.py][4]（封装base64模块 - Encapsulate the module）
 - [demo2.py][5]（使用BaseUtil类 - Use the BaseUtil class）

### 参考博客
[【廖雪峰的官方网站】Python内建模块 Base64][6]

[【CSDN viclee108】关于Base64编码的理解][7]

[【博客园 luguo3000】从原理上搞定Base64编码][8]


  [1]: https://raw.githubusercontent.com/scriptgeeker/python-demo/master/__CDN__/Base64-principle.png
  [2]: https://github.com/scriptgeeker/python-demo/blob/master/BaseCode/demo1.py
  [3]: https://github.com/scriptgeeker/python-demo/blob/master/BaseCode/mybase.py
  [4]: https://github.com/scriptgeeker/python-demo/blob/master/BaseCode/base.py
  [5]: https://github.com/scriptgeeker/python-demo/blob/master/BaseCode/demo2.py
  [6]: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000
  [7]: https://blog.csdn.net/goodlixueyong/article/details/52132250
  [8]: http://www.cnblogs.com/luguo3000/p/3940197.html