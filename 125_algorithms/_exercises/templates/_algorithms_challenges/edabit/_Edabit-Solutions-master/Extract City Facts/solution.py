___ city_facts(city):
    for i in city:
        __ i == "name":
            c = city[i]
        elif i == "population":
            p = city[i]
        else:
            co = city[i]
    return ("{} has a population of {} and is situated in {}".format(c,p,co))
