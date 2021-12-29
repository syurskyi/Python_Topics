#Please download the database file database.db and and the ten_more_countries.txt file. Then, add the rows of the text file to the database file.
_______ sqlite3
_______ pandas

data  pandas.read_csv("ten_more_countries.txt")

conn  sqlite3.connect("database.db")
cur  conn.cursor()
___ index, row __ data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))
conn.commit()
conn.close()
