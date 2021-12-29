'''
Created on Mar 4, 2018

@author: tongq
'''
class Interval(object):
    ___ __init__(self, start, end):
        self.start = start
        self.end = end

class MyCalendar(object):

    ___ __init__(self):
        self.intervals = []

    ___ book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        newInterval = Interval(start, end)
        for i, interval in enumerate(self.intervals):
            __ newInterval.end <= interval.start:
                self.intervals.insert(i, newInterval)
                return True
            elif newInterval.start >= interval.end:
                continue
            else:
                return False
        self.intervals.append(newInterval)
        return True

__ __name__ == '__main__':
    cal = MyCalendar()
    print(cal.book(10, 20))
    print(cal.book(15, 25))
    print(cal.book(20, 30))
