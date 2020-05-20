import sqlite3

conn = sqlite3.connect('db.sqlite3')

conn.execute('CREATE TABLE "users" (id, first_name, last_name, birthday)')
conn.execute('SELECT * FROM "users"')
conn.execute(
    """INSERT INTO users(id, first_name, last_name, birthday) 
       VALUES (1, "Eugene", "Petrov", "09-11-1992")
    """
)
conn.execute(
    """INSERT INTO users(id, first_name, last_name, birthday)
       VALUES (2, "Viktor", "Ivanov", "10-11-1992"),
              (3, "Dmitry", "Sidorov", "11-09-1992")
    """
)

users = conn.execute('SELECT * FROM "users"').fetchall()
print(users)
cursor = conn.execute('SELECT * from "users";')
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
# cursor.close()

try:
    cursor = conn.execute('SELECT * FROM "tags"')
except sqlite3.OperationalError as e:
    print(e)

first_name = 'Dmitry'
sql_text = 'SELECT * FROM users WHERE first_name = "%s"' % (first_name,)
print(sql_text)
first_name = '"Dmitry"'
sql_text = 'SELECT * FROM users WHERE first_name = "%s"' % (first_name,)
print(sql_text)

sql_text = 'SELECT * FROM "users" WHERE id = %s' % (10,)
print(sql_text)
sql_text2 = 'SELECT * FROM "users" WHERE id = %s' % ('0 or id like "%"',)
print(sql_text)

cursor.execute('SELECT * FROM "users" WHERE id = ?', (10,))
cursor.execute('SELECT * FROM "users" WHERE id = :id', {'id': 10})
conn.close()
