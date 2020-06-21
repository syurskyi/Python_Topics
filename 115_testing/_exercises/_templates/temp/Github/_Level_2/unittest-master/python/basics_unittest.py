# assignment03unittest.py
# @author:        Shubham Sachdeva
# @email:
# @date:          18-10-09

# reads data from input.csv
# For simplicity reads only ['GEO'], ['DGUID'], ['Food categories'], ['Commodity'] fields
# class Product - a class defining a record
# def read_csv - function that reads data from given file
# def main - main function

______ csv
______ u__

CONST_AUTHOR _ "Shubham Sachdeva"

c_ TestFunc?.?
    ___ testAuthor
        aE..(author(), CONST_AUTHOR)

    ___ testRead
        aE..(le.(read_csv('input.csv')), 30559)

___ author(
    print ('Author: ', CONST_AUTHOR)
    r_ CONST_AUTHOR

c_ Product:
    # initialisation
    ___  -   year, geo, guid, category, commodity
        id _ 0
        year _ __.(year)
        geo _ geo
        guid _ guid
        category _ category
        commodity _ commodity

    # for print
    ___ -s
        r_ ("%d\t%d\t%s\t%s\t%s\t%s" % (id, year, geo, guid, category, commodity))


___ read_csv(file_name
    lst _ # list
    ___
        w__ o..(file_name, newline_'', encoding_'utf-8') __ csvfile:
            reader _ csv.DictReader(csvfile)
            ___ row __ reader:
                product _ Product(1960, row['GEO'], row['DGUID'], row['Food categories'], row['Commodity'])
                print (product)
                lst.a..(product)

    _____:
        print ('read_csv failed')

    r_ lst

__ _____ __ _____
    ?.?
