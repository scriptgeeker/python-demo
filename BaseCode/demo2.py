try:
    from .base import BaseUtil
except:
    exec('from base import BaseUtil')

# 实例化 BaseUtil 对象
base16 = BaseUtil(BaseUtil.BASE16)
base32 = BaseUtil(BaseUtil.BASE32)
base64 = BaseUtil(BaseUtil.BASE64)
base85 = BaseUtil(BaseUtil.BASE85)

# URL安全的Base64编码
urlsafe = BaseUtil(BaseUtil.URLSAFE)

# 字节数组编码与解码
print(BaseUtil().encode(b'Python'))  # b'UHl0aG9u'
print(BaseUtil().decode(b'UHl0aG9u'))  # b'Python'

# 字符串编码与解码
print(BaseUtil().encodeStr('君の名は'))  # 5ZCb44Gu5ZCN44Gv
print(BaseUtil().decodeStr('5ZCb44Gu5ZCN44Gv'))  # 君の名は

# 文件编码与解码
with open('src/avatar.base', 'wb') as fwb:
    fwb.write(BaseUtil().encodeFile('src/avatar.jpg'))
with open('src/avatar.jpg', 'wb') as fwb:
    fwb.write(BaseUtil().decodeFile('src/avatar.base'))
