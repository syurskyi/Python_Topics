import sqlite3

# connect to database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Delete Records
c.execute("DELETE from customers WHERE rowid = 6")

conn.commit()

# Query The Database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close()
