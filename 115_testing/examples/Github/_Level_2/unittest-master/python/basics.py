# assignment03.py
# @author:        Shubham Sachdeva
# @email:
# @date:          18-10-09

import csv

CONST_AUTHOR = "Shubham Sachdeva"

# REF_DATE	GEO	DGUID	Food categories	Commodity
class Product:
    # initialisation
    def __init__(self, year, geo, guid, category, commodity):
        self.id = 0
        self.year = int(year)
        self.geo = geo
        self.guid = guid
        self.category = category
        self.commodity = commodity

    # for print
    def __str__(self):
        return ("%d\t%d\t%s\t%s\t%s\t%s" % (self.id, self.year, self.geo, self.guid, self.category, self.commodity))


def read_csv(file_name):
    lst = []
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(1960, row['GEO'], row['DGUID'], row['Food categories'], row['Commodity'])
                print (product)
                lst.append(product)

    except:
        print ('read_csv failed')

    return lst

def main():
    lst = read_csv('input.csv')
    n = len(lst)
    print ('Number of records: ', n)
    if n < 10000:
        print ('There are less than 10000 records')
    elif n > 10000:
        print ('There are more than 10000 records')
    else:
        print ('There are exactly 10000 records')

if __name__ == '__main__':
    print (CONST_AUTHOR)
    main()
