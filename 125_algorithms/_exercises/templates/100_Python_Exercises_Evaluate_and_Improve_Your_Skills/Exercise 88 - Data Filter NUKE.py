#Create a script that uses countries_by_area.txt file as data sourcea and prints out the top 5 most densely populated countries

_______ pandas

data  pandas.read_csv("countries_by_area.txt")
data["density"]  data["population_2013"] / data["area_sqkm"]
data  data.sort_values(by"density", ascendingFalse)

___ index, row __ data[:5].iterrows():
    print(row["country"])
