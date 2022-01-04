____ c.. _______ defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

___ group_names_by_country(data: s.. = data) __ defaultdict:
    countries = defaultdict(l..)
    data = i..(data.splitlines())
    next(data)
    ___ line __ data:
        lastname, name, country = line.s..(",")
        countries[country].a..(f"{name} {lastname}")
    r.. s..(countries.i..
