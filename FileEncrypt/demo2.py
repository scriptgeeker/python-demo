import os

try:
    from .fsecure import FileSecure
except:
    exec('from fsecure import FileSecure')

directory = input('Enter Folder Path:').replace('\\', '/')
fileSec = FileSecure(maxsize=100)
# 遍历整个目录，找出所有文件
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filename, filesize = fileSec.handle(filepath, FileSecure.RE)
        print(filename, '-', filesize)
