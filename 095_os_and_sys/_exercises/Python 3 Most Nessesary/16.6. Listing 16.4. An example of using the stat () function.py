import os, time
s = os.stat(r"file.txt")
s
# nt.stat_result(st_mode=33060, st_ino=2251799813878096, st_dev=0,
# st_nlink=1, st_uid=0, st_gid=0, st_size=18, st_atime=1304111982,
# st_mtime=1304044731, st_ctime=1304028509)
s.st_size      # Размер файла
# 18
t = s.st_atime # Время последнего доступа к файлу
time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t))
# '30.04.2011 01:19:42'
t = s.st_ctime # Время создания файла
time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t))
# '29.04.2011 02:08:29'
t = s.st_mtime # Время последнего изменения файла
time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t))
# '29.04.2011 06:38:51'
