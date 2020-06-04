______ sqlite3
connection _ sqlite3.c__("projects.db")
cursor _ connection.c__
cursor.e..("""
    CREATE TABLE projects
    (url TEXT, descr TEXT, income INTEGER)
""")
cursor.e..("""INSERT INTO projects VALUES 
    ('giraffes.io', 'Uber, but with giraffes', 1900),
    ('dronesweaters.com', 'Clothes for cold drones', 3000),
    ('hummingpro.io', 'Online humming courses', 120000)
""")
connection.c__