## 文件加密

使用AES-CBC模式对文件进行加密和解密

----------

### 核心原理

高级加密标准（Advanced Encryption Standard，AES），是美国联邦政府采用的一种区块加密标准。这个标准用来替代原先的DES，已然成为对称密钥加密中最流行的算法之一。

AES只是个基本算法，实现AES有若干模式。其中的CBC模式因为其安全性而被 TLS 和 IPSec 作为技术标准。

CBC模式对于每个待加密的密码块在加密前会先与前一个密码块的密文异或然后再用加密器加密。CBC模式相比ECB有更高的保密性，但由于对每个数据块的加密依赖与前一个数据块的加密所以加密无法并行。

### 三方模块

PyCrypto 已死，请替换为 PyCryptodome 

```
pip install pycryptodome    # 加密算法模块
```

### 文件索引

 - [demo1.py][1]（AES模块使用示范 - Encryption module demo）
 - [cryptor.py][2]（AES-CBC Encryption and decryption tool）
 - [fsecure.py][3]（文件加密工具 - File security encryption tool）
 - [demo2.py][4]（加密整个目录 - Handling files under the directory）

### 参考博客
[【CSDN melody_sy】python3.6 实现AES加密][5]

[【CSDN charleslei】高级加密标准AES的工作模式][6]


  [1]: https://github.com/scriptgeeker/python-demo/blob/master/FileEncrypt/demo1.py
  [2]: https://github.com/scriptgeeker/python-demo/blob/master/FileEncrypt/cryptor.py
  [3]: https://github.com/scriptgeeker/python-demo/blob/master/FileEncrypt/fsecure.py
  [4]: https://github.com/scriptgeeker/python-demo/blob/master/FileEncrypt/demo2.py
  [5]: https://blog.csdn.net/s740556472/article/details/78778522
  [6]: https://blog.csdn.net/charleslei/article/details/48710293