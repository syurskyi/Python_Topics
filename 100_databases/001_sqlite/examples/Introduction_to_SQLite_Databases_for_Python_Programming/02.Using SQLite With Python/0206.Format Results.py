import sqlite3

# connect to database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query The Database
c.execute("SELECT * FROM customers")
# print(c.fetchall())
# print(c.fetchone())
# print(c.fetchone()[3])
# print(c.fetchmany(3))

items = c.fetchall()
# print(items)
for item in items:
    print(item)

print()

for item in items:
    print(item[0])

print()

for item in items:
    print(item[0] + " " + item[1] + " " + item[2])

print()

for item in items:
    print(item[0] + " " + item[1] + " | " + item[2])

print()

print("NAME " + "\t\t\t\tEMAIL")
print("-------" + "\t\t\t\t------")
for item in items:
    print(item[0] + " " + item[1] + "\t\t\t" + item[2])

# Commit our command
conn.commit()

# Close our connection
conn.close()
