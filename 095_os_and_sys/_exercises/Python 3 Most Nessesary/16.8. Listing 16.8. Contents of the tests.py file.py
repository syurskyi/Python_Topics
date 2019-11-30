# -*- coding: utf-8 -*-

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break


# C:\Python34\python.exe tests.py < file.txt


# -*- coding: utf-8 -*-
print("String")            # Эта строка будет записана в файл


# C:\Python34\python.exe tests.py > file.txt

# C:\Python34\python.exe tests.py >> file.txt