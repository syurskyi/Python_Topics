import shutil      # Подключаем модуль
shutil.copyfile(r"file.txt", r"file2.txt")
# Путь не существует:
shutil.copyfile(r"file.txt", r"C:\book2\file2.txt")
# ... Фрагмент опущен ...
# FileNotFoundError: [Errno 2] No such file or directory:
# 'C:\\book2\\file2.txt'

shutil.copy(r"file.txt", r"file3.txt")

shutil.copy2(r"file.txt", r"file4.txt")

shutil.move(r"file4.txt", r"C:\book\test")


import os  # Подключаем модуль
try:
    os.rename(r"file3.txt", "file4.txt")
except OSError:
    print("Файл не удалось переименовать")
else:
    print("Файл успешно переименован")


os.remove(r"file2.txt")
os.unlink(r"file4.txt")

import os.path
os.path.exists(r"file.txt"), os.path.exists(r"file2.txt")
# (True, False)
os.path.exists(r"C:\book"), os.path.exists(r"C:\book2")
# (True, False)
#

os.path.getsize(r"file.txt")  # Файл существует
# 18
os.path.getsize(r"file2.txt") # Файл не существует
# ... Фрагмент опущен ...
# OSError: [Error 2] Не удается найти указанный файл: 'file2.txt'


import time    # Подключаем модуль time
t = os.path.getatime(r"file.txt")
t
# 1304111982.96875
time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t))
# '30.04.2011 01:19:42'


t = os.path.getctime(r"file.txt")
t
# 1304028509.015625
time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t))
# '29.04.2011 02:08:29'


t = os.path.getmtime(r"file.txt")
t
# 1304044731.265625
time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t))
# '29.04.2011 06:38:51'