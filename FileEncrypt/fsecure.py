import os
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64


class FileSecure():
    RE, EN, DE = 0, 1, 2  # replace, encrypt, decrypt

    def __init__(self, suffix='oaa', maxsize=10):
        self.__salt = 'one-above-all'  # Cipher salt
        self.__suffix = suffix  # Encrypted file suffix
        self.__maxsize = maxsize * 1024 ** 2  # File size limit MB

    # get key from the file name
    def __getKey(self, filepath):
        filename = os.path.basename(filepath)
        suffix = '.' + self.__suffix
        if filename[-len(suffix):] == suffix:
            filename = filename[:-len(suffix)]
        tmpstr = filename + self.__salt
        md5, sha1 = hashlib.md5(), hashlib.sha1()
        md5.update(tmpstr.encode('utf8'))
        sha1.update(md5.hexdigest().encode())
        return sha1.hexdigest().upper()[:16].encode()

    # AES-CBC Encrypt
    def __encrypt(self, text, key):
        if len(text) % 16 != 0:
            text += (16 - len(text) % 16) * b'\x00'
        aes = AES.new(key, AES.MODE_CBC, key)
        return aes.encrypt(text)

    # AES-CBC Decrypt
    def __decrypt(self, ciphertext, key):
        aes = AES.new(key, AES.MODE_CBC, key)
        text = aes.decrypt(ciphertext)
        return text.strip(b'\x00')

    # File Secure Encrypt
    def __fileEnc(self, filepath):
        key = self.__getKey(filepath)
        with open(filepath, 'rb') as frb:
            text = frb.read()
        text = b2a_base64(text)
        ciphertext = self.__encrypt(text, key)
        with open(filepath, 'wb') as fwb:
            fwb.write(ciphertext)
        newpath = filepath + '.' + self.__suffix
        os.rename(filepath, newpath)
        return newpath

    # File Secure Decrypt
    def __fileDec(self, filepath):
        key = self.__getKey(filepath)
        with open(filepath, 'rb') as frb:
            ciphertext = frb.read()
        text = self.__decrypt(ciphertext, key)
        text = a2b_base64(text)
        with open(filepath, 'wb') as fwb:
            fwb.write(text)
        newpath = filepath[:-(len(self.__suffix) + 1)]
        os.rename(filepath, newpath)
        return newpath

    # Encrypt or Decrypt Execute
    def handle(self, filepath, mode=0):
        filepath = os.path.abspath(filepath)
        suffix = os.path.splitext(filepath)[1]
        if mode != self.DE and suffix != '.' + self.__suffix:
            if os.path.getsize(filepath) < self.__maxsize:
                filepath = self.__fileEnc(filepath)
        if mode != self.EN and suffix == '.' + self.__suffix:
            filepath = self.__fileDec(filepath)
        return os.path.basename(filepath), os.path.getsize(filepath)


if __name__ == '__main__':
    fileSec = FileSecure(suffix='oaa', maxsize=10)
    if os.path.exists('README.md'):
        filepath = 'README.md'
    else:
        filepath = 'README.md.oaa'
    filename, filesize = fileSec.handle(filepath, FileSecure.RE)
    print(filename, filesize)
