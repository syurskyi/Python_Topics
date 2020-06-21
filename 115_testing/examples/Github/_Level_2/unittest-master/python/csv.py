# assignment04.py
# @author:        Shubham Sachdeva
# @email:
# @date:          18-11-09

# reads data from input.csv
# For simplicity reads only ['GEO'], ['DGUID'], ['Food categories'], ['Commodity'] fields
# class Product - a class defining a record
# def read_csv - function that reads data from given file


import csv
import _mysql

import bisect

CONST_AUTHOR = "Shubham Sachdeva"

# Uses mysql database connection.
# Class Database simply wraps basic CRUD operations.
class Database:
    # Establishing a mysql connection
    def __init__(self):
        self.db = _mysql.connect("localhost", "root", "root", "student")
        self._tablename = ""

    # insert a record
    def create(self, product):
        query = ("INSERT INTO %s (geo, guid, category, commodity) VALUES('%s', '%s', '%s', '%s')" %
            (self._tablename, product.geo, product.guid, product.category, product.commodity))
        self.db.query(query)

    # update a record based on id
    def update(self, id, product):
        query = ("UPDATE %s SET geo='%s', guid='%s', category='%s', commodity='%s' WHERE id=%d" %
            (self._tablename, product.geo, product.guid, product.category, product.commodity, product.id))
        self.db.query(query)

    # get a record based on id
    def read(self, id):
        query = "SELECT * FROM %s WHERE id=%d" % (self._tablename, id)
        self.db.query(query)
        r = self.db.store_result()
        product = Product()
        for i in r.fetch_row(maxrows=1):
            product.id = int(i[0])
            product.geo = i[1]
            product.guid = i[2]
            product.category = i[3]
            product.commodity = i[4]
        return product

    # delete a record based on id
    def delete(self, id):
        self.db.query("""DELETE FROM %s WHERE id=%d""" % (self._tablename, id))

    # create table if it doesn't exist
    def select_table(self, tablename):
        self.db.query(
            "CREATE TABLE IF NOT EXISTS " + tablename + " (`id` INT NOT NULL AUTO_INCREMENT ,  "
                                                        "`geo` VARCHAR(30) NOT NULL , "
                                                        "`guid` VARCHAR(30) NOT NULL , "
                                                        "`category` VARCHAR(100) NOT NULL , "
                                                        "`commodity` VARCHAR(100) NOT NULL , "
                                                        "PRIMARY KEY (`id`)) ENGINE = InnoDB;")
        self._tablename = tablename

# custom sort function
# sort by guid
def cmpFn(obj):
    return obj.guid

# Class List - Custom list using standard list API library.
# Member function find and reverse_find returns index of given element.
# While find returns leftmost position, reverse_find returns rightmost position.
# This assumes that the list is sorted.
class List:
    def __init__(self):
        self.lst = []
        self.lstguid = []

    def append(self, obj):
        self.lst.append(obj)

    def sort(self):
        self.lst = sorted(self.lst, key=cmpFn)
        self.lstguid = [obj.guid for obj in self.lst ]

    def find(self, guid):
        return bisect.bisect_left(self.lstguid, guid)

    def reverse_find(self, guid):
        return bisect.bisect_right(self.lstguid, guid)

# list iterator
# ListIterator simply operates on a list of primitive types.
class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cur = 0

    def get(self):
        if self.cur >=0 and self.cur < len(self.lst):
            return self.lst[self.cur]
        else:
            return None

    def next(self):
        if self.cur < len(self.lst) -1:
            self.cur += 1
            return True
        else:
            return False

    def prev(self):
        if self.cur > 0:
            self.cur -= 1
            return True
        else:
            return False

    def info(self):
        return str(self.get())

# inherited from ListIterator
# Member function info has been overriden.
class ObjectListIterator(ListIterator):
    def info(self):
        obj = self.get()
        if obj == None:
            return "None"
        return "Current Object: " + ("%d\t%s\t%s\t%s\t%s" % (self.id, self.geo, self.guid, self.category, self.commodity))

class Product:
    # initialisation
    def __init__(self, geo, guid, category, commodity):
        self.id = 0
        self.geo = geo
        self.guid = guid
        self.category = category
        self.commodity = commodity

    # for print
    def __str__(self):
        return ("%d\t%s\t%s\t%s\t%s" % (self.id, self.geo, self.guid, self.category, self.commodity))

# reads 4 fields from given file
def read_csv(file_name):
    lst = []
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(row['GEO'], row['DGUID'], row['Food categories'], row['Commodity'])
                print (product)
                lst.append(product)

    except:
        print ('read_csv failed')

    return lst

def main():
    lst = read_csv('input.csv')
    n = len(lst)

    db = Database()
    db.select_table('products')

    for item in lst:
        pass
        db.create(item)

    print("Created " + str(len(lst)) + " items");

    print("Programmed by " + CONST_AUTHOR)

if __name__ == '__main__':
    print (CONST_AUTHOR)
    main()
