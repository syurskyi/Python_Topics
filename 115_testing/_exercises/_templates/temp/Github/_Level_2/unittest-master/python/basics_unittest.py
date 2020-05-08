# assignment03unittest.py
# @author:        Shubham Sachdeva
# @email:
# @date:          18-10-09

# reads data from input.csv
# For simplicity reads only ['GEO'], ['DGUID'], ['Food categories'], ['Commodity'] fields
# class Product - a class defining a record
# def read_csv - function that reads data from given file
# def main - main function

import csv
import unittest

CONST_AUTHOR = "Shubham Sachdeva"

c_ TestFunc(unittest.TestCase):
    ___ testAuthor(self):
        self.assertEqual(author(), CONST_AUTHOR)

    ___ testRead(self):
        self.assertEqual(len(read_csv('input.csv')), 30559)

___ author():
    print ('Author: ', CONST_AUTHOR)
    return CONST_AUTHOR

c_ Product:
    # initialisation
    ___  -   year, geo, guid, category, commodity):
        self.id = 0
        self.year = int(year)
        self.geo = geo
        self.guid = guid
        self.category = category
        self.commodity = commodity

    # for print
    ___ __str__(self):
        return ("%d\t%d\t%s\t%s\t%s\t%s" % (self.id, self.year, self.geo, self.guid, self.category, self.commodity))


___ read_csv(file_name):
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

if __name__ == '__main__':
    unittest.main()
