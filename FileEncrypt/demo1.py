from Crypto.Cipher import AES

# 密钥，必须为16位字节
key = b'www.poxiaoshifen.ac.cn'

# key是16位, 其对应为 AES-128
key = (key + 16 * b'\x00')[:16]
print(key)

aes = AES.new(key, AES.MODE_CBC, key)  # 密钥，加密模式，初始向量

# 加密内容，需为字节类型
text = '这是我们所笃信的，而且是我们所追求的'.encode('utf8')

# 添加空字节使其为16位倍数
while len(text) % 16 != 0:
    text += b'\x00'
print(text)

# 将拼接后的内容传入加密类中
ciphertext = aes.encrypt(text)
print(ciphertext)

# decrypt() cannot be called after encrypt()
aes = AES.new(key, AES.MODE_CBC, key)  # 密钥，加密模式，初始向量

# 用aes对象进行解密
text = aes.decrypt(ciphertext)

# 去除添加的空字节
text = text.replace(b'\x00', b'')

# 打印解密后的字符串
print(text.decode('utf8'))
