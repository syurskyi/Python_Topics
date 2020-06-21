import sqlite3

# connect to database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

many_customer = [
    ('Wes', 'Brown', 'john@comedy.com'),
    ('Steph', 'Kuewa', 'steph@comedy.com'),
    ('Dan', 'Pas', 'dan@comedy.com'),
]

# Create a Table
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customer)


print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()
