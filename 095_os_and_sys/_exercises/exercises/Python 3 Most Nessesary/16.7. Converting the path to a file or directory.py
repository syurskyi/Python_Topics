# # # -*- coding: utf-8 -*-
#
# # abspath ( <Относительный путь>) - преобразует относительный путь в абсоmотный, учитывая
# # местоположение текущего рабочего каталога.
# # в относительном пути можно указать как прямые, так и обратные"
# # слеши. Все они будут автоматически преобразованы с учетом значения атрибута
# # sep из модуля os. path. Значение этого атрибута зависит от используемой операционной
# # системы. Выведем значение атрибута sep в операционной системе Windows:
# # При указании пути в Windows следует учитывать, что слеш является специальным символом.
# # По этой причине слеш необходимо удваивать (экранировать) или вместо обычных строк использовать неформатированные
# # строки.
# # Кроме того, если слеш расположен в конце строки, то его необходимо удваивать даже при использовании
# # неформатированных строк:
# # isabs (<Путь>) - возвращает True, если путь является абсолютным, и False - в противном
# # случае:
# # basename (<Путь>) - возвращает имя файла без пути к нему:
# # dirname (<Путь>) - возвращает путь к папке, где хранится файл:
# # split (<Путь>) - возвращает кортеж из двух элементов: пути к папке, где хранится
# # файл, и названия файла:
# # splitdrive (<Путь>) - разделяет путь на имя диска и остальную часть пути. В качестве
# # значения возвращается кортеж из двух элементов
# # splitext (<Путь>) - возврашает кортеж из двух элементов: пути с названием файла, но
# # без расширения, и расширения файла ( фрагмент после последней точки)
# # join(<Пyтьl>[, ... , <ПутьN>]) - соединяет указанные элементы пути, при необходимости
# # вставляя между ними разделители:
# # Обратите внимание на последний пример - в пути используются разные слеши, и в результате
# # получен некорректный путь. Чтобы этот путь сделать корректным, необходимо
# # воспользоваться функцией norrnpath ( ) :
#
# ______ __.p___
# __.p___.a.. _ file.txt
# # 'C:\\book\\file.txt'
# __.p___.a.. _ folder1/file.txt
# # 'C:\\book\\folder1\\file.txt'
# __.p___.a.. _ ../file.txt
# # 'C:\\file.txt'
#
#
# __.p___.sep
# # '\\'
#
# # "C:\\temp\\new\\file.txt"    # Правильно
# # 'C:\\temp\\new\\file.txt'
# # _"C:\temp\new\file.txt"      # Правильно
# # 'C:\\temp\\new\\file.txt'
# # "C:\temp\new\file.txt"       # Неправильно!!!
# # 'C:\temp\new\x0cile.txt'
# # ######################################################################################################################
#
# # _"C:\temp\new\"              # Неправильно!!!
# # SyntaxError: EOL while scanning string literal
# # _"C:\temp\new\\"
# # 'C:\\temp\\new\\\\'
# # ######################################################################################################################
#
# # "C:\\temp\\new\\"            # Правильно
# # 'C:\\temp\\new\\'
# # _"C:\temp\new\\"[:-1]        # Можно и удалить слэш
# # 'C:\\temp\\new\\'
# # ######################################################################################################################
# __.p___.is.. _ C:\book\file.txt
# # True
# __.p___.is..  file.txt
# # False
# # ######################################################################################################################
#
# __.p___.b.. _ C:\book\folder1\file.txt
# # 'file.txt'
# __.p___.b.. _ C:\book\folder
# # 'folder'
# __.p___.b..  C:\\book\\folder\\
# # ''
# # ######################################################################################################################
#
# __.p___.d.. _ C:\book\folder\file.txt
# # 'C:\\book\\folder'
# __.p___.d.. _ C:\book\folder
# # 'C:\\book'
# __.p___.d.. C:\\book\\folder\\
# # 'C:\\book\\folder'
# # ######################################################################################################################
#
# __.p___.s.. _ C:\book\folder\file.txt
# # ('C:\\book\\folder', 'file.txt')
# __.p___.s.. _ C:\book\folder
# # ('C:\\book', 'folder')
# __.p___.s.. C:\\book\\folder\\
# # ('C:\\book\\folder', '')
# # ######################################################################################################################
#
# __.p___.s.d._ C:\book\folder\file.txt
# # ('C:', '\\book\\folder\\file.txt')
# # ######################################################################################################################
#
# __.p___.splitext _ C:\book\folder\file.tar.gz
# # ('C:\\book\\folder\\file.tar', '.gz')
# # ######################################################################################################################
#
# __.p___.j.. C:\\   book\\folder   file.txt
# # 'C:\\book\\folder\\file.txt'
# __.p___.j.. _ C:\\   book/folder/   file.txt
# # 'C:\\\\book/folder/file.txt'
# # ######################################################################################################################
#
# p = __.p___.j..(_ C:\\   book/folder/   file.txt )
# __.p___.n..(p)
# # 'C:\\book\\folder\\file.txt'
# # ######################################################################################################################