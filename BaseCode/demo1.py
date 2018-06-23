import base64

# 内建模块的使用
text = 'Base64编码用于传输8Bit字节代码'
print(text)

text_bit = bytes(text, 'utf8') or text.encode('utf8')
print(text_bit)

text_b64 = base64.b64encode(text_bit)
print(text_b64)

text_bit = base64.b64decode(text_b64)
print(text_bit)

text = str(text_bit, 'utf8') or text_bit.decode('utf8')
print(text)
