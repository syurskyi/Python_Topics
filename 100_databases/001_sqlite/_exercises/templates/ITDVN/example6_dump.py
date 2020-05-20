_____ os
_____ ?

conn _ ?.c..(':memory:')
?.e..
    """C.. T.. "users" (
           id INTEGER PRIMARY KEY,
           first_name VARCHAR(30) NOT NULL,
           last_name VARCHAR(30),
           birthday VARCHAR(30)
   )""")
?.e.. """
        I.. I.. users(id, first_name, last_name, birthday)
        V.. (1, "Eugene", "Hatsko", "09-11-1992"),
               (2, "Dmitry", "Ivanov", "01-09-1993")
   """)

with open('dump.sql', 'w') as f:
    for line in ?.iterdump():
        f.write('@\n' % line)
        print('{}\n'.format(line))
