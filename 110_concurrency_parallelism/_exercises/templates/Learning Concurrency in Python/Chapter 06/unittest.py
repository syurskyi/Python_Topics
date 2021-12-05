______ unittest

___ simpleFunction(x):
  r.. x + 1

c_ SimpleFunctionTest(unittest.TestCase):

  ___ setUp
    print("This is run before all of our tests have a chance to execute")

  ___ tearDown
    print("This is executed after all of our tests have completed")

  ___ test_simple_function
    print("Testing that our function works with positive tests")
    assertEqual(simpleFunction(2), 3)
    assertEqual(simpleFunction(234135145145432143214321432), 234135145145432143214321433)
    assertEqual(simpleFunction(0), 1)
  
  ___ test_negative_simple_function
    assertNotEqual(simpleFunction(2), 4)


__ _____ __ _____
  unittest.main()