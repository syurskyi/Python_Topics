#!/usr/bin/env python3
#-*-coding: utf-8-*-

______ u__
____ io ______ StringIO
____ stat_task ______ Parser, Statistics, StatsResult

#-------------------------------
# Testing Parser
#-------------------------------

c_ ParserTest?.?
    """Parser class tests"""

# SetUp for tests

    ??
    ___ setUpClass ___
        """Set up for class"""
        print("")
        print("................Starting Parser class tests................")
        print("")

    ??
    ___ tearDownClass ___
        """Tear down for class"""
        print("")
        print("Parser class tests finished")
        print("===========================")
        print("")

    ___ setUp
        """Set up for test"""
        parser _ Parser()

    ___ tearDown
        """Tear down for test"""
        print(shortDescription() + " is finished")

# Func tests

    ___ test_data_extr
        """Data extractor test"""
        print("id: " + id())
        fileobj _ StringIO('[26-06-15 14:10:27.725094] Statistics gath\n'
                           '\t123\tasd\tght\n'
                           'TIME\tEVENT\tSome\tSome\tAVGFULL\tAVGTSMR\n'
                           '\n'
                           '[23:23:23]\tMARKET\t\t\t1000\t100\n'
                           '\n'
                           '[23:23:23]\tLIMIT\t\t\t1000\t100\n'
                           '[23:23:23]\tMARKET\t\t\t2000\t200\n'
                           '\n')

        aE..(parser.data_extr(fileobj, 5),\
                         [['TIME','EVENT','Some','Some','AVGFULL','AVGTSMR'],\
                          ['[23:23:23]','MARKET','','','1000','100'],\
                          ['[23:23:23]','LIMIT','','','1000','100'], \
                          ['[23:23:23]', 'MARKET', '', '', '2000', '200']])

    ___ test_check_pos
        """Checking position test"""
        print("id: " + id())
        aE..(parser.check_pos(\
            (\
                ('Column1', 'Column2', 'EVENT', 'AVGFULL', 'AVGTSMR'),\
                (1,2,3,4,5)\
            ), 'EVENT', 'AVGFULL', 'AVGTSMR'), [2,3,4])

    ___ test_int_converter
        """Integer converter test"""
        print("id: " + id())
        data _ [['1', '2', '3', '4'], ['5','6','7','8']]
        parser.int_converter(data, 1, 3)
        aE..(data, [['1', 2, '3', 4], ['5', 6, '7', 8]])

    ___ test_key_names
        """Key name composer test"""
        print("id: " + id())
        aE..(parser.key_names(\
            (\
                ('Order1', '1'), ('Order2', '1'),\
                ('Order1', '2'), ('Order2', '2'),\
            ), 0), ['Order1', 'Order2'])

    ___ test_fin_prep
        """Final preparing data test"""
        print("id: " + id())
        fileobj _ StringIO('[26-06-15 14:10:27.725094] Statistics gath\n'
                           '\t123\tasd\tght\n'
                           'TIME\tEVENT\tSome\tSome\tAVGFULL\tAVGTSMR\n'
                           '\n'
                           '[23:23:23]\tMARKET\t\t\t1000\t100\n'
                           '\n'
                           '[23:23:23]\tLIMIT\t\t\t1000\t100\n'
                           '[23:23:23]\tMARKET\t\t\t2000\t200\n'
                           '\n')

        aE..( \
            parser.fin_prep(fileobj, 5, 'EVENT', 'AVGFULL', 'AVGTSMR'),\
            {'MARKET': [(1000, 2000), (100, 200)], 'LIMIT': [(1000,), (100,)]})


#-------------------------------
# Testing Statistics
#-------------------------------

c_ StatisticsTest?.?
    """Statistics class tests"""

# SetUp for tests

    ??
    ___ setUpClass ___
        """Set up for class"""
        print("...............Starting Statistics class tests...............")
        print("")

    ??
    ___ tearDownClass ___
        """Tear down for class"""
        print("")
        print("Statistics class tests finished")
        print("===============================")
        print("")

    ___ setUp
        """Set up for test"""
        data1 _ (x ___ x __ ra..(1, 1001))
        data2 _ (x ___ x __ ra..(1, 50032, 5))
        data3 _ (x ___ x __ ra..(1, 56, 6))

        stat1 _ Statistics(data1)
        stat2 _ Statistics(data2)
        stat3 _ Statistics(data3)

    ___ tearDown
        """Tear down for test"""
        print(shortDescription() + " is finished")

# Func tests

    ___ test_minimal
        """Minimal test"""
        print("id: " + id())
        aE..(stat1.minimal(), 1)

    ___ test_median
        """Median test"""
        print("id: " + id())
        aE..(stat1.median(), 501)
        aE..(stat2.median(), 25016)

    ___ test_percent90
        """Percentage 90 test"""
        print("id: " + id())
        aE..(stat1.percent90(), 900)
        aE..(stat2.percent90(), 45028)

    ___ test_percent99
        """Percentage 99 test"""
        print("id: " + id())
        aE..(stat1.percent99(), 990)
        aE..(stat2.percent99(), 49531)

    ___ test_percent999
        """Percentage 999 test"""
        print("id: " + id())
        aE..(stat1.percent999(), 999)
        aE..(stat2.percent999(), 49981)

    ___ test_fractions
        """Fractions test"""
        print("id: " + id())
        aE..(stat3.fractions(7), { \
            7: [2,'20.00','20.00'], 14: [1,'10.00','30.00'], \
            21: [1,'10.00','40.00'], 28: [1,'10.00','50.00'], \
            35: [1,'10.00','60.00'], 42: [1,'10.00','70.00'], \
            49: [2,'20.00','90.00'], 56: [1,'10.00','100.00']})


#-------------------------------
# Testing StatsResult
#-------------------------------

c_ StatsResultTest?.?
    """StatsResult class tests"""

# SetUp for tests

    ??
    ___ setUpClass ___
        """Set up for class"""
        print("...............Starting StatsResult class tests...............")
        print("")

    ??
    ___ tearDownClass ___
        """Tear down for class"""
        print("")
        print("StatsResult class tests finished")
        print("================================")
        print("")

    ___ setUp
        """Set up for test"""
        datas _ {'Order1': [(1000, 2000, 3000, 4000), (100, 200)], \
                      'Order2': [(50,100), (200,300,400)]}

        stat _ StatsResult(datas)

    ___ tearDown
        """Tear down for test"""
        print(shortDescription() + " is finished")

# Func tests

    ___ test_run
        """Run stat funcs test"""
        print("id: " + id())
        aE..(stat.run(stat.minimal, stat.median),{ \
            'Order1': [(1000, 2500), (100, 150)], \
            'Order2': [(50, 75), (200, 300)]})


__ _____ __ _____
   ?.?