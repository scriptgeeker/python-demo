from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class Cryptor():

    def __init__(self, key: str):
        self.__mode = AES.MODE_CBC
        self.__key = self.setKey(key)

    def setKey(self, key: str):
        key = key.encode('utf8')
        key = (key + 16 * b'\x00')[:16]
        return key

    def setText(self, text: str):
        text = text.encode('utf8')
        while len(text) % 16 != 0:
            text += b'\x00'
        return text

    def encrypt(self, text: str):
        aes = AES.new(self.__key, self.__mode, self.__key)
        ciphertext = aes.encrypt(self.setText(text))
        return b2a_hex(ciphertext)

    def decrypt(self, ciphertext: str):
        aes = AES.new(self.__key, self.__mode, self.__key)
        text = aes.decrypt(a2b_hex(ciphertext))
        text = text.rstrip(b'\x00')
        return text.decode('utf8')


if __name__ == '__main__':
    text = '富强、民主、文明、和谐，自由、平等、公正、法治， 爱国、敬业、诚信、友善'
    cryptor = Cryptor(key='社会主义核心价值观')
    ciphertext = cryptor.encrypt(text=text)
    print(ciphertext)
    text = cryptor.decrypt(ciphertext=ciphertext)
    print(text)
