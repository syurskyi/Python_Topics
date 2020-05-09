# Filename: test_suite_regression.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is to combine all test into a regression testing suite

#______ unit test framework and all individual test cases
______ unittest
______ add_singlenode_unittest
______ deleting_nodes_unittest
______ getting_size_of_linkedlist_unittest
  
#Load all the test cases
suiteList _ []
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(add_singlenode_unittest.SingleNodeInsertionTest))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(deleting_nodes_unittest.NodesDeleteTest))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(getting_size_of_linkedlist_unittest.SizeOfLinkedList))

#Join the test and running them
comboSuite _ unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity_2).run(comboSuite)
