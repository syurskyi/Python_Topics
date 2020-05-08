"""
 https://github.com/lathama/python-testing-example
"""

from testingdemo.howto import AnExample
import unittest

c_ TestAnExample(unittest.TestCase):

    ___ setUp(self):
        self.theclass = AnExample()
        self.epochtime = 123456789
        self.epochtimepriorday = 123370389

    ___ test_make_something(self):
        result = self.theclass.make_something()
        self.assertTrue(result)

    ___ test_report_something(self):
        self.theclass.rightnow = self.epochtime
        self.theclass.yesterdaythistime = self.epochtimepriorday
        result = self.theclass.report_something()
        goal = self.theclass.descriptiontext + str(self.epochtime) 
        goal += " and " + str(self.epochtimepriorday)
        self.assertEqual(goal, result)

    ___ test_should_fail(self):
        self.assertTrue(self.theclass.should_fail())
    
#badspacesandfileendlinemakestylecheckunhappy