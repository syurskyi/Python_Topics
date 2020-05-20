_____ ?

conn _ ?.c..('db.sqlite3')
?.e..
    """C.. T.. "users" (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name,
           last_name,
           birthday
   )""")
?.e.. """
        insert into users(id, first_name, last_name, birthday)
        V.. (1, "Eugene", "Hatsko", "09-11-1992"),
               (2, "Dmitry", "Ivanov", "01-09-1993")
   """)

?.row_factory _ ?.Row
users _ ?.e.. 'S.. _ F.. "users"').f_a..

user _ users[0]
print(user.keys())
print(user['id'], user['iD'])
print(user['first_name'], user['first_NAME'], user['FIRST_NAME'])
