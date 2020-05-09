# assignment04.py
# @author:        Shubham Sachdeva
# @email:
# @date:          18-11-09

# reads data from input.csv
# For simplicity reads only ['GEO'], ['DGUID'], ['Food categories'], ['Commodity'] fields
# class Product - a class defining a record
# def read_csv - function that reads data from given file


______ csv
______ _mysql
______ unittest

______ bisect

CONST_AUTHOR _ "Shubham Sachdeva"

c_ TestList(unittest.TestCase):
    ___ testAuthor
        assertEqual(author(), CONST_AUTHOR)

    ___ testList
        lst _ List()
        lst.append(Product("Canada", "3333", "Food", "AAA"))
        lst.append(Product("Canada", "5555", "Food", "AAA"))
        lst.append(Product("Canada", "8888", "Food", "AAA"))
        lst.sort()
        assertEqual(lst.find("5555"), 1)

___ author():
    print('Author: ', CONST_AUTHOR)
    r_ CONST_AUTHOR


# Uses mysql database connection.
# Class Database simply wraps basic CRUD operations.
c_ Database:
    # Establishing a mysql connection
    ___  - 
        db _ _mysql.connect("localhost", "root", "root", "student")
        _tablename _ ""

    # insert a record
    ___ create  product):
        query _ ("INSERT INTO %s (geo, guid, category, commodity) VALUES('%s', '%s', '%s', '%s')" %
            (_tablename, product.geo, product.guid, product.category, product.commodity))
        db.query(query)

    # update a record based on id
    ___ update  id, product):
        query _ ("UPDATE %s SET geo='%s', guid='%s', category='%s', commodity='%s' WHERE id=%d" %
            (_tablename, product.geo, product.guid, product.category, product.commodity, product.id))
        db.query(query)

    # get a record based on id
    ___ read  id):
        query _ "SELECT * FROM %s WHERE id=%d" % (_tablename, id)
        db.query(query)
        r _ db.store_result()
        product _ Product()
        for i in r.fetch_row(maxrows_1):
            product.id _ int(i[0])
            product.geo _ i[1]
            product.guid _ i[2]
            product.category _ i[3]
            product.commodity _ i[4]
        r_ product

    # delete a record based on id
    ___ delete  id):
        db.query("""DELETE FROM %s WHERE id=%d""" % (_tablename, id))

    # create table if it doesn't exist
    ___ select_table  tablename):
        db.query(
            "CREATE TABLE IF NOT EXISTS " + tablename + " (`id` INT NOT NULL AUTO_INCREMENT ,  "
                                                        "`geo` VARCHAR(30) NOT NULL , "
                                                        "`guid` VARCHAR(30) NOT NULL , "
                                                        "`category` VARCHAR(100) NOT NULL , "
                                                        "`commodity` VARCHAR(100) NOT NULL , "
                                                        "PRIMARY KEY (`id`)) ENGINE = InnoDB;")
        _tablename _ tablename

# custom sort function
# sort by guid
___ cmpFn(obj):
    r_ obj.guid

# Class List - Custom list using standard list API library.
# Member function find and reverse_find returns index of given element.
# While find returns leftmost position, reverse_find returns rightmost position.
# This assumes that the list is sorted.
c_ List:
    ___  - 
        lst _ []
        lstguid _ []

    ___ append  obj):
        lst.append(obj)

    ___ sort
        lst _ sorted(lst, key_cmpFn)
        lstguid _ [obj.guid for obj in lst ]

    ___ find  guid):
        r_ bisect.bisect_left(lstguid, guid)

    ___ reverse_find  guid):
        r_ bisect.bisect_right(lstguid, guid)

# list iterator
# ListIterator simply operates on a list of primitive types.
c_ ListIterator:
    ___  -   lst):
        lst _ lst
        cur _ 0

    ___ get
        if cur >_0 and cur < len(lst):
            r_ lst[cur]
        else:
            r_ None

    ___ next
        if cur < len(lst) -1:
            cur +_ 1
            r_ True
        else:
            r_ False

    ___ prev
        if cur > 0:
            cur -_ 1
            r_ True
        else:
            r_ False

    ___ info
        r_ str(get())

# inherited from ListIterator
# Member function info has been overriden.
c_ ObjectListIterator(ListIterator):
    ___ info
        obj _ get()
        if obj == None:
            r_ "None"
        r_ "Current Object: " + ("%d\t%s\t%s\t%s\t%s" % (id, geo, guid, category, commodity))

c_ Product:
    # initialisation
    ___  -   geo, guid, category, commodity):
        id _ 0
        geo _ geo
        guid _ guid
        category _ category
        commodity _ commodity

    # for print
    ___ __str__
        r_ ("%d\t%s\t%s\t%s\t%s" % (id, geo, guid, category, commodity))

# reads 4 fields from given file
___ read_csv(file_name):
    lst _ []
    try:
        with open(file_name, newline_'', encoding_'utf-8') as csvfile:
            reader _ csv.DictReader(csvfile)
            for row in reader:
                product _ Product(row['GEO'], row['DGUID'], row['Food categories'], row['Commodity'])
                # print (product)
                lst.append(product)

    except:
        print ('read_csv failed')

    r_ lst

___ main():
    lst _ read_csv('input.csv')
    n _ len(lst)

    db _ Database()
    db.select_table('products')

    for item in lst:
        pass
        db.create(item)


if __name__ == '__main__':
    unittest.main()
