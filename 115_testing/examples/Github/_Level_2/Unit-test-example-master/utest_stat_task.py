#!/usr/bin/env python3
#-*-coding: utf-8-*-

import unittest
from io import StringIO
from stat_task import Parser, Statistics, StatsResult

#-------------------------------
# Testing Parser
#-------------------------------

class ParserTest(unittest.TestCase):
    """Parser class tests"""

# SetUp for tests

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("")
        print("................Starting Parser class tests................")
        print("")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("")
        print("Parser class tests finished")
        print("===========================")
        print("")

    def setUp(self):
        """Set up for test"""
        self.parser = Parser()

    def tearDown(self):
        """Tear down for test"""
        print(self.shortDescription() + " is finished")

# Func tests

    def test_data_extr(self):
        """Data extractor test"""
        print("id: " + self.id())
        fileobj = StringIO('[26-06-15 14:10:27.725094] Statistics gath\n'
                           '\t123\tasd\tght\n'
                           'TIME\tEVENT\tSome\tSome\tAVGFULL\tAVGTSMR\n'
                           '\n'
                           '[23:23:23]\tMARKET\t\t\t1000\t100\n'
                           '\n'
                           '[23:23:23]\tLIMIT\t\t\t1000\t100\n'
                           '[23:23:23]\tMARKET\t\t\t2000\t200\n'
                           '\n')

        self.assertEqual(self.parser.data_extr(fileobj, 5),\
                         [['TIME','EVENT','Some','Some','AVGFULL','AVGTSMR'],\
                          ['[23:23:23]','MARKET','','','1000','100'],\
                          ['[23:23:23]','LIMIT','','','1000','100'], \
                          ['[23:23:23]', 'MARKET', '', '', '2000', '200']])

    def test_check_pos(self):
        """Checking position test"""
        print("id: " + self.id())
        self.assertEqual(self.parser.check_pos(\
            (\
                ('Column1', 'Column2', 'EVENT', 'AVGFULL', 'AVGTSMR'),\
                (1,2,3,4,5)\
            ), 'EVENT', 'AVGFULL', 'AVGTSMR'), [2,3,4])

    def test_int_converter(self):
        """Integer converter test"""
        print("id: " + self.id())
        self.data = [['1', '2', '3', '4'], ['5','6','7','8']]
        self.parser.int_converter(self.data, 1, 3)
        self.assertEqual(self.data, [['1', 2, '3', 4], ['5', 6, '7', 8]])

    def test_key_names(self):
        """Key name composer test"""
        print("id: " + self.id())
        self.assertEqual(self.parser.key_names(\
            (\
                ('Order1', '1'), ('Order2', '1'),\
                ('Order1', '2'), ('Order2', '2'),\
            ), 0), ['Order1', 'Order2'])

    def test_fin_prep(self):
        """Final preparing data test"""
        print("id: " + self.id())
        fileobj = StringIO('[26-06-15 14:10:27.725094] Statistics gath\n'
                           '\t123\tasd\tght\n'
                           'TIME\tEVENT\tSome\tSome\tAVGFULL\tAVGTSMR\n'
                           '\n'
                           '[23:23:23]\tMARKET\t\t\t1000\t100\n'
                           '\n'
                           '[23:23:23]\tLIMIT\t\t\t1000\t100\n'
                           '[23:23:23]\tMARKET\t\t\t2000\t200\n'
                           '\n')

        self.assertEqual( \
            self.parser.fin_prep(fileobj, 5, 'EVENT', 'AVGFULL', 'AVGTSMR'),\
            {'MARKET': [(1000, 2000), (100, 200)], 'LIMIT': [(1000,), (100,)]})


#-------------------------------
# Testing Statistics
#-------------------------------

class StatisticsTest(unittest.TestCase):
    """Statistics class tests"""

# SetUp for tests

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("...............Starting Statistics class tests...............")
        print("")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("")
        print("Statistics class tests finished")
        print("===============================")
        print("")

    def setUp(self):
        """Set up for test"""
        self.data1 = (x for x in range(1, 1001))
        self.data2 = (x for x in range(1, 50032, 5))
        self.data3 = (x for x in range(1, 56, 6))

        self.stat1 = Statistics(self.data1)
        self.stat2 = Statistics(self.data2)
        self.stat3 = Statistics(self.data3)

    def tearDown(self):
        """Tear down for test"""
        print(self.shortDescription() + " is finished")

# Func tests

    def test_minimal(self):
        """Minimal test"""
        print("id: " + self.id())
        self.assertEqual(self.stat1.minimal(), 1)

    def test_median(self):
        """Median test"""
        print("id: " + self.id())
        self.assertEqual(self.stat1.median(), 501)
        self.assertEqual(self.stat2.median(), 25016)

    def test_percent90(self):
        """Percentage 90 test"""
        print("id: " + self.id())
        self.assertEqual(self.stat1.percent90(), 900)
        self.assertEqual(self.stat2.percent90(), 45028)

    def test_percent99(self):
        """Percentage 99 test"""
        print("id: " + self.id())
        self.assertEqual(self.stat1.percent99(), 990)
        self.assertEqual(self.stat2.percent99(), 49531)

    def test_percent999(self):
        """Percentage 999 test"""
        print("id: " + self.id())
        self.assertEqual(self.stat1.percent999(), 999)
        self.assertEqual(self.stat2.percent999(), 49981)

    def test_fractions(self):
        """Fractions test"""
        print("id: " + self.id())
        self.assertEqual(self.stat3.fractions(7), { \
            7: [2,'20.00','20.00'], 14: [1,'10.00','30.00'], \
            21: [1,'10.00','40.00'], 28: [1,'10.00','50.00'], \
            35: [1,'10.00','60.00'], 42: [1,'10.00','70.00'], \
            49: [2,'20.00','90.00'], 56: [1,'10.00','100.00']})


#-------------------------------
# Testing StatsResult
#-------------------------------

class StatsResultTest(unittest.TestCase):
    """StatsResult class tests"""

# SetUp for tests

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("...............Starting StatsResult class tests...............")
        print("")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("")
        print("StatsResult class tests finished")
        print("================================")
        print("")

    def setUp(self):
        """Set up for test"""
        self.datas = {'Order1': [(1000, 2000, 3000, 4000), (100, 200)], \
                      'Order2': [(50,100), (200,300,400)]}

        self.stat = StatsResult(self.datas)

    def tearDown(self):
        """Tear down for test"""
        print(self.shortDescription() + " is finished")

# Func tests

    def test_run(self):
        """Run stat funcs test"""
        print("id: " + self.id())
        self.assertEqual(self.stat.run(self.stat.minimal, self.stat.median),{ \
            'Order1': [(1000, 2500), (100, 150)], \
            'Order2': [(50, 75), (200, 300)]})


if __name__ == '__main__':
   unittest.main()