# # -*- coding: utf-8 -*-

import os
os.getcwd()               # Текущий рабочий каталог
# 'C:\\book'


os.chdir("C:\\book\\folder1\\")
os.getcwd()               # Текущий рабочий каталог
# 'C:\\book\\folder1'
# ######################################################################################################################

os.mkdir("newfolder")     # Создание каталога
os.rmdir("newfolder") # Удаление каталога

os.listdir("C:\\book\\folder1\\")
# ['file1.txt', 'file2.txt', 'file3.txt', 'folder1', 'folder2']
# ######################################################################################################################

for (p, d, f) in os.walk("C:\\book\\folder1\\"):
    print(p)

# C:\book\folder1\
# C:\book\folder1\folder1_1
# C:\book\folder1\folder1_1\folder1_1_1
# C:\book\folder1\folder1_1\folder1_1_2
# C:\book\folder1\folder1_2
# ######################################################################################################################

for (p, d, f) in os.walk("C:\\book\\folder1\\", False):
    print(p)

# C:\book\folder1\folder1_1\folder1_1_1
# C:\book\folder1\folder1_1\folder1_1_2
# C:\book\folder1\folder1_1
# C:\book\folder1\folder1_2
# C:\book\folder1\
# ######################################################################################################################


import os
for (p, d, f) in os.walk("C:\\book\\folder1\\", False):
    for file_name in f: # Удаляем все файлы
        os.remove(os.path.join(p, file_name))
    for dir_name in d: # Удаляем все каталоги
        os.rmdir(os.path.join(p, dir_name))


import shutil
shutil.rmtree("C:\\book\\folder1\\")


from os.path import normcase
normcase(r"c:/BoOk/fIlE.TxT")
# 'c:\\book\\file.txt'
# ######################################################################################################################

import os.path
os.path.isdir(r"C:\book\file.txt")
# False
os.path.isdir("C:\\book\\")
# True
# ######################################################################################################################

os.path.isfile(r"C:\book\file.txt")
# True
os.path.isfile("C:\\book\\")
# False
# ######################################################################################################################