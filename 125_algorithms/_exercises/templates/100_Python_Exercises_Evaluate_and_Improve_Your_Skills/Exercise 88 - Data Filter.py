#Create a script that uses countries_by_area.txt file as data sourcea and prints out the top 5 most densely populated countries

______ pandas

data _ pandas.read_csv("countries_by_area.txt")
data["density"] _ data["population_2013"] / data["area_sqkm"]
data _ data.sort_values(by_"density", ascending_False)

___ index, row __ data[:5].iterrows
    print(row["country"])
