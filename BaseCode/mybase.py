'''
base64编解码原理
The principle of Base64 codec
'''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
           'abcdefghijklmnopqrstuvwxyz' + \
           '0123456789' + '+/'

alpdic = {'{:0>6}'.format(bin(i)[2:]): alphabet[i] for i in range(len(alphabet))}
bindic = {alphabet[i]: '{:0>6}'.format(bin(i)[2:]) for i in range(len(alphabet))}


# 十六进制转二进制
def hex2bin(_hex: str):
    form = '{:0>%d}' % (len(_hex) * 4)
    return form.format(bin(int(_hex, 16))[2:])


# 二进制转十六进制
def bin2hex(_bin: str):
    form = '{:0>%d}' % (len(_bin) // 4)
    return form.format(hex(int(_bin, 2))[2:])


# Base64编码
def encode(_bytes: bytes):
    fill = 0  # 填充0字节数
    # 二进制数据是否为3的倍数
    if len(_bytes) % 3 != 0:
        # 用\x00字节在末尾补足
        fill = (3 - len(_bytes) % 3)
        _bytes += b'\x00' * fill
    _base = b''  # 转换后的 Base64 字节码
    # 循环取出 3 Byte(3*8 bit)
    for i in range(0, len(_bytes), 3):
        binary = hex2bin(_bytes[i:i + 3].hex())
        # 3*8 bit转 4*6 bit
        for j in range(0, len(binary), 6):
            _base += alpdic[binary[j:j + 6]].encode('ascii')
    if fill != 0:  # "="表示所添加的零值字节数
        return _base[:-fill] + (b'=' * fill)
    return _base


# Base64解码
def decode(_base: bytes):
    bindic['='] = '000000'
    fill = _base[-3:].count(b'=')  # 获得零字节填充数
    _bytes = b''  # 解码后的字节数据
    # 循环取出 4 Byte(4*6bit)
    for i in range(0, len(_base), 4):
        binary = ''  # 二进制序列
        for b in _base[i:i + 4]:
            binary += bindic[chr(b)]
        #  4*6 bit转 3*8 bit
        for j in range(0, len(binary), 8):
            _hex = bin2hex(binary[j:j + 8])
            _bytes += bytes.fromhex(_hex)
    if fill != 0:  # 去除填充在末尾的零字节
        return _bytes[:-fill]
    return _bytes


if __name__ == '__main__':
    import base64

    _bytes = '自定义Base64编码和解码'.encode()
    base_1 = base64.b64encode(_bytes)
    base_2 = encode(_bytes)
    print('Encode Correct:', base_1 == base_2)

    _base = 'QmFzZTY057yW56CB55So5LqO5Lyg6L6TOEJpdOWtl+iKguS7o+eggQ=='.encode()
    bytes_1 = base64.b64decode(_base)
    bytes_2 = decode(_base)
    print('Decode Correct:', bytes_1 == bytes_2)
