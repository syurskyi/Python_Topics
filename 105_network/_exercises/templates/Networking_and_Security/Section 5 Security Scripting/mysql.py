______ MySQLdb

___
    db _ MySQLdb.c..(host_"localhost", user_"ric", p__swd_"P4ssw0rd!", db_"myDB")

    curs _ db.cursor

    curs.ex..("select * from tblGrades")

    ___ row __ curs.fetchall
        print("Name: @, Grade: @"  (row[1], row[2]))

______ E.. __ e:
    print(e)

