# assignment03.py
# @author:        Shubham Sachdeva
# @email:
# @date:          18-10-09

______ csv

CONST_AUTHOR _ "Shubham Sachdeva"

# REF_DATE	GEO	DGUID	Food categories	Commodity
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

___ main(
    lst _ read_csv('input.csv')
    n _ le.(lst)
    print ('Number of records: ', n)
    __ n < 10000:
        print ('There are less than 10000 records')
    elif n > 10000:
        print ('There are more than 10000 records')
    ____:
        print ('There are exactly 10000 records')

__ _____ __ _____
    print (CONST_AUTHOR)
    main()
