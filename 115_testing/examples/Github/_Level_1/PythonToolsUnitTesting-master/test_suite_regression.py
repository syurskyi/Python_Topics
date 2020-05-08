# Filename: test_suite_regression.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is to combine all test into a regression testing suite

#import unit test framework and all individual test cases
import unittest
import add_singlenode_unittest
import deleting_nodes_unittest
import getting_size_of_linkedlist_unittest
  
#Load all the test cases
suiteList = []
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(add_singlenode_unittest.SingleNodeInsertionTest))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(deleting_nodes_unittest.NodesDeleteTest))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(getting_size_of_linkedlist_unittest.SizeOfLinkedList))

#Join the test and running them
comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=2).run(comboSuite)
