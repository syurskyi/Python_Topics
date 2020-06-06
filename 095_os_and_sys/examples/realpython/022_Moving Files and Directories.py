# To move a file or directory to another location, use shutil.move(src, dst).
#
# src is the file or directory to be moved and dst is the destination:
#
# >>> import shutil
# >>> shutil.move('dir_1/', 'backup/')
# 'backup'
#
# shutil.move('dir_1/', 'backup/') moves dir_1/ into backup/ if backup/ exists. If backup/ does not exist,
# dir_1/ will be renamed to backup.

