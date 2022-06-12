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

____ c.. _______ d..

# fake data from https://www.mockaroo.com
data """last_name,first_name,country_code
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


___ group_names_by_country(data: s.. data) __ d..:
    countries d.. l..
    # you code
    split_lines ?.s..
    line_cnt 0
    ___ line __ split_lines:
        print(line)
        __ line_cnt __ 0:
            line_cnt += 1
            _____
        arr ?.s.. ','
        print(arr)
        name arr[1] + " " + arr[0]
        ___
            countries[arr[2]].a..(name)
        ______:
            l    # list
            l.a..(name)
            countries[arr[2]] l
        _______
            line_cnt += 1
    r.. countries


print(group_names_by_country(data


