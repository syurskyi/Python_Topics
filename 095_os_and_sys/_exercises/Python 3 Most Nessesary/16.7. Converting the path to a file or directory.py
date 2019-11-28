import os.path
os.path.abspath(r"file.txt")
# 'C:\\book\\file.txt'
os.path.abspath(r"folder1/file.txt")
# 'C:\\book\\folder1\\file.txt'
os.path.abspath(r"../file.txt")
# 'C:\\file.txt'


os.path.sep
# '\\'

"C:\\temp\\new\\file.txt"    # Правильно
# 'C:\\temp\\new\\file.txt'
r"C:\temp\new\file.txt"      # Правильно
# 'C:\\temp\\new\\file.txt'
"C:\temp\new\file.txt"       # Неправильно!!!
# 'C:\temp\new\x0cile.txt'


r"C:\temp\new\"              # Неправильно!!!
# SyntaxError: EOL while scanning string literal
r"C:\temp\new\\"
# 'C:\\temp\\new\\\\'


"C:\\temp\\new\\"            # Правильно
# 'C:\\temp\\new\\'
r"C:\temp\new\\"[:-1]        # Можно и удалить слэш
# 'C:\\temp\\new\\'

os.path.isabs(r"C:\book\file.txt")
# True
os.path.isabs("file.txt")
# False

os.path.basename(r"C:\book\folder1\file.txt")
# 'file.txt'
os.path.basename(r"C:\book\folder")
# 'folder'
os.path.basename("C:\\book\\folder\\")
# ''


os.path.dirname(r"C:\book\folder\file.txt")
# 'C:\\book\\folder'
os.path.dirname(r"C:\book\folder")
# 'C:\\book'
os.path.dirname("C:\\book\\folder\\")
# 'C:\\book\\folder'


os.path.split(r"C:\book\folder\file.txt")
# ('C:\\book\\folder', 'file.txt')
os.path.split(r"C:\book\folder")
# ('C:\\book', 'folder')
os.path.split("C:\\book\\folder\\")
# ('C:\\book\\folder', '')


os.path.splitdrive(r"C:\book\folder\file.txt")
# ('C:', '\\book\\folder\\file.txt')


os.path.splitext(r"C:\book\folder\file.tar.gz")
# ('C:\\book\\folder\\file.tar', '.gz')


os.path.join("C:\\", "book\\folder", "file.txt")
# 'C:\\book\\folder\\file.txt'
os.path.join(r"C:\\", "book/folder/", "file.txt")
# 'C:\\\\book/folder/file.txt'


p = os.path.join(r"C:\\", "book/folder/", "file.txt")
os.path.normpath(p)
# 'C:\\book\\folder\\file.txt'