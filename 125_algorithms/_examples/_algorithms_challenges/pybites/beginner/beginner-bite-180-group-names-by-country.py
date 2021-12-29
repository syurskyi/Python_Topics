"""
In this Bite you are presented with a list of surnames, names, and countries. 
These 3 fields are in a multiline string, separated by a comma.

Code group_names_by_country, looping through the list, 
returning a collections.defaultdict where the keys are countries and the values 
are lists of concatenated names and surnames. The order of the names does not matter.

Here is an example of a possible input to your function:

data = last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN
... and the output your function should return:

defaultdict(,
            {'BR': ['Alphonso Harrold'],
             'CN': ['Margo Apdell', 'Ines Parrett', 'Davie Halbard'],
             'ID': ['Husain Watsham', 'Sula Wasielewski'],
             'PL': ['Kermit Braunle'],
             'RU': ['Deerdre Tomblings'],
             'SE': ['Luke Brenston'],
             'TD': ['Rudolph Jeffry']})
"""

from collections import defaultdict

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
    countries = defaultdict(list)
    # you code
    split_lines = data.splitlines()
    line_cnt = 0
    for line in split_lines:
        print(line)
        if line_cnt == 0:
            line_cnt += 1
            continue
        arr = line.split(',')
        print(arr)
        name = arr[1] + " " + arr[0]
        try:
            countries[arr[2]].append(name)
        except:
            l = []
            l.append(name)
            countries[arr[2]] = l
        finally:
            line_cnt += 1
    return countries


print(group_names_by_country(data))


