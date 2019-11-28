import os, time
os.stat(r"file.txt")          # Первоначальные значения
# nt.stat_result(st_mode=33060, st_ino=2251799813878096, st_dev=0,
# st_nlink=1, st_uid=0, st_gid=0, st_size=18, st_atime=1304111982,
# st_mtime=1304044731, st_ctime=1304028509)
t = time.time() - 600
os.utime(r"file.txt", (t, t))  # Текущее время минус 600 сек
os.stat(r"file.txt")
# nt.stat_result(st_mode=33060, st_ino=2251799813878096, st_dev=0,
# st_nlink=1, st_uid=0, st_gid=0, st_size=18, st_atime=1304112906,
# st_mtime=1304112906, st_ctime=1304028509)
os.utime(r"file.txt", None)   # Текущее время
os.stat(r"file.txt")
# nt.stat_result(st_mode=33060, st_ino=2251799813878096, st_dev=0,
# st_nlink=1, st_uid=0, st_gid=0, st_size=18, st_atime=1304113557,
# st_mtime=1304113557, st_ctime=1304028509)
