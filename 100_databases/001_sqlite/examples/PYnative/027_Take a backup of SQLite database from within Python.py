import sqlite3

def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

try:
    #existing DB
    sqliteCon = sqlite3.connect('SQLite_Python.db')
    #copy into this DB
    backupCon = sqlite3.connect('Sqlite_backup.db')
    with backupCon:
        sqliteCon.backup(backupCon, pages=3, progress=progress)
    print("backup successful")
except sqlite3.Error as error:
    print("Error while taking backup: ", error)
finally:
    if(backupCon):
        backupCon.close()
        sqliteCon.close()


# Output:
#
# Copied 3 of 26 pages...
# Copied 6 of 26 pages...
# Copied 9 of 26 pages...
# Copied 12 of 26 pages...
# Copied 15 of 26 pages...
# Copied 18 of 26 pages...
# Copied 21 of 26 pages...
# Copied 24 of 26 pages...
# Copied 26 of 26 pages...
# backup successful