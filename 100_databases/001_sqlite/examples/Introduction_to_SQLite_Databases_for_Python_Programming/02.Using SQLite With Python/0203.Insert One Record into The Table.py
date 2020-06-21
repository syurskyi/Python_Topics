import sqlite3

# connect to database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a Table
c.execute('INSERT INTO customers VALUES ("John", "Elder,", "john@comedy.com")')
c.execute('INSERT INTO customers VALUES ("Tim", "Smith,", "tim@comedy.com")')
c.execute('INSERT INTO customers VALUES ("Mary", "Bown,", "mary@comedy.com")')

print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()
