import base64


class BaseUtil(object):
    BASE16 = (base64.b16encode, base64.b16decode)
    BASE32 = (base64.b32encode, base64.b32decode)
    BASE64 = (base64.b64encode, base64.b64decode)
    BASE85 = (base64.b85encode, base64.b85decode)
    URLSAFE = (base64.urlsafe_b64decode, base64.urlsafe_b64decode)

    def __init__(self, mode=BASE64):
        self.__encode = mode[0]
        self.__decode = mode[1]

    def encode(self, _bytes: bytes):
        return self.__encode(_bytes)

    def decode(self, _bytes: bytes):
        return self.__decode(_bytes)

    def encodeStr(self, _str: str):
        return self.__encode(_str.encode()).decode()

    def decodeStr(self, _str: str):
        return self.__decode(_str.encode()).decode()

    def encodeFile(self, filepath):
        with open(filepath, 'rb') as frb:
            return self.__encode(frb.read())

    def decodeFile(self, filepath):
        with open(filepath, 'rb') as frb:
            return self.__decode(frb.read())
