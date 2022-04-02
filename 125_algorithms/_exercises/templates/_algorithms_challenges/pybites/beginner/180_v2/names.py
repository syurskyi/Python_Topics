____ c.. _______ defaultdict
_______ i..

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
    
    result = defaultdict(l..)
    lines = data.s..
    
    ___ i __ r..(1,l..(lines)):
        last_name,first_name,country = lines[i].s..(',')
        result[country].a..(first_name + ' ' + last_name)


    r.. result






__ _______ __ _______

    group_names_by_country()
