import sqlite3

# connect to database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Drop Table

c.execute("DROP TABLE customers")
conn.commit()

# c.execute("SELECT rowid, * FROM customers LIMIT 2")
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close()
