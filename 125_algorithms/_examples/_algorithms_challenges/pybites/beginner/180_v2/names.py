from collections import defaultdict
import itertools

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


def group_names_by_country(data: str = data) -> defaultdict:
    
    result = defaultdict(list)
    lines = data.splitlines()
    
    for i in range(1,len(lines)):  
        last_name,first_name,country = lines[i].split(',')
        result[country].append(first_name + ' ' + last_name)


    return result






if __name__ == "__main__":

    group_names_by_country()
