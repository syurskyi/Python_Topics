_____ ?

___ progress(status, remaining, total
    print(f'Copied {total-remaining} of {total} pages...')

___
    #existing DB
    sqliteCon _ ?.c..('SQLite_Python.db')
    #copy into this DB
    backupCon _ ?.c..('Sqlite_backup.db')
    w__ backupCon:
        sqliteCon.backup(backupCon, pages_3, progress_progress)
    print("backup successful")
_____ ?.E.. __ error:
    print("Error while taking backup: " ?
f..
    __(backupCon
        backupCon.c..
        sqliteCon.c..


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