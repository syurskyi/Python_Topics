____ collections _______ defaultdict

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


___ group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(l..)
    ___ line __ data.split('\n')[1:]:
        lname, fname, country = line.split(',')
        countries[country].a..(f"{fname} {lname}")
    r.. countries

group_names_by_country()