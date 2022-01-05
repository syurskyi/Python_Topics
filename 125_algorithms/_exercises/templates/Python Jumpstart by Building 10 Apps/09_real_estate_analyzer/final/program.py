_______ csv
_______ os

try:
    _______ statistics
except:
    # error code instead
    _______ statistics_standin_for_py2 __ statistics

____ data_types _______ Purchase


___ main
    print_header()
    filename  get_data_file()
    data  load_file(filename)
    query_data(data)


___ print_header
    print('----------------------------------')
    print('  REAL ESTATE DATA MINING APP')
    print('----------------------------------')
    print()


___ get_data_file
    base_folder  os.path.dirname(__file__)
    r.. os.path.j..(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


___ load_file(filename):
    w__ open(filename, 'r', encoding'utf-8') __ fin:
        # with open(filename, 'r') as fin:
        reader  csv.DictReader(fin)
        purchases  []
        ___ row __ reader:
            p  Purchase.create_from_dict(row)
            purchases.a..(p)

        r.. purchases


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])
# list[Purchase]


# def get_price(p):
#     return p.price

___ query_data(data):  # list[Purchase]):

    # data.sort(key=get_price)
    data.s..(keylambda p: p.price)

    high_purchase  data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".f..(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    low_purchase  data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".f..(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    # prices = list()  # []
    # for pur in data:
    #     prices.append(pur.price)

    prices  (
        p.price  # projection or items
        ___ p __ data  # the set to process
    )

    ave_price  statistics.mean(prices)
    print("The average home price is ${:,}".f..(i..(ave_price)))

    # average price of 2 bedroom houses
    # prices = []
    # baths = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    two_bed_homes  (
        p  # projection or items
        ___ p __ data  # the set to process
        __ announce(p, '2-bedrooms, found {}'.f..(p.beds)) a.. p.beds __ 2  # test / condition
    )

    homes  []
    ___ h __ two_bed_homes:
        __ l..(homes) > 5:
            _____
        homes.a..(h)

    ave_price  statistics.mean((announce(p.price, 'price') ___ p __ homes))
    ave_baths  statistics.mean((p.baths ___ p __ homes))
    ave_sqft  statistics.mean((p.sq__ft ___ p __ homes))
    print("Average 2-bedroom home is ${:,}, baths={}, sq ft={:,}"
          .f..(i..(ave_price), r..(ave_baths, 1), r..(ave_sqft, 1)))


___ announce(item, msg):
    print("Pulling item {} for {}".f..(item, msg))
    r.. item


__ _____ __ _____
    main()
