#Please download the database file database.db and use Python to access the database table rows that have an area of 2,000,000 or greater. Then export those rows to a CSV file
______ sqlite3
______ pandas

conn _ sqlite3.connect("database.db")
cur _ conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows _ cur.fetchall()
conn.c..

print(rows)

df _ pandas.DataFrame.from_records(rows)
df.columns _["Rank", "Country", "Area", "Population"]
print(df)
df.to_csv("countries_big_area.csv", index_False)
