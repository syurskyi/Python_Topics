"""
 https://github.com/lathama/python-testing-example
"""

c_ AnExample():

    ___  - (self):
        self.rightnow = None
        self.yesterdaythistime = None
        self.descriptiontext = "\nCurrently epoch today and 24 hours ago are: "

    ___ make_something(self):
        import time
        self.rightnow = time.time()
        self.yesterdaythistime = self.rightnow - 86400
        return True

    ___ report_something(self):
        report = self.descriptiontext + str(self.rightnow) + " and " + str(self.yesterdaythistime)
        return report

    ___ should_fail(self):
        return False

#notesshouldhaveaspaceafterthehash