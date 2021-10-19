# #Please download the database file database.db and use Python to access the database table rows that have an area of 2,000,000 or greater. Then export those rows to a CSV file
# _______ ?
# _______ pandas
#
# conn = ?.c..  database.db
# cur = c...c..
# c__.e..("SELECT * FROM countries WHERE area >= 2000000")
# rows = c__.f..
# c...c..
#
# print ?
#
# df = pandas.DataFrame.from_records(rows)
# df.columns =["Rank", "Country", "Area", "Population"]
# print(df)
# df.to_csv("countries_big_area.csv", index=False)
