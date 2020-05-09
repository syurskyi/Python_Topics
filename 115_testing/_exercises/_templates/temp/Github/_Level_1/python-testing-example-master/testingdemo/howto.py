"""
 https://github.com/lathama/python-testing-example
"""

c_ AnExample(

    ___  -
        rightnow _ None
        yesterdaythistime _ None
        descriptiontext _ "\nCurrently epoch today and 24 hours ago are: "

    ___ make_something
        ______ time
        rightnow _ time.time()
        yesterdaythistime _ rightnow - 86400
        r_ T..

    ___ report_something
        report _ descriptiontext + st.(rightnow) + " and " + st.(yesterdaythistime)
        r_ report

    ___ should_fail
        r_ F..

#notesshouldhaveaspaceafterthehash