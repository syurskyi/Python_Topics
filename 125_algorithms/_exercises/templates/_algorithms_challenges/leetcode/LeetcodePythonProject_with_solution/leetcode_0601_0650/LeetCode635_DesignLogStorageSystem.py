'''
Created on Sep 24, 2017

@author: MT
'''
class LogSystem(object):
    ___ __init__(self):
        self.units = {
            'Year': 4,
            'Month': 7,
            'Day': 10,
            'Hour': 13,
            'Minute':16,
            'Second':19
            }
        self.timestamps = []

    ___ put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.timestamps.append((id, timestamp))

    ___ retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res = []
        idx = self.units[gra]
        for timestamp in self.timestamps:
            __ timestamp[1][:idx] >= s[:idx] and\
                timestamp[1][:idx] <= e[:idx]:
                res.append(timestamp[0])
        return res

__ __name__ == '__main__':
    log = LogSystem()
    log.put(1, "2017:01:01:23:59:59")
    log.put(2, "2017:01:01:22:59:59")
    log.put(3, "2016:01:01:00:00:00")
    print(log.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))
    print(log.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))
    print('-='*30+'-')
    
#     log = LogSystem()
#     log.put(1,"2017:01:01:23:59:59")
#     log.put(2,"2017:01:02:23:59:59")
#     print(log.retrieve("2017:01:01:23:59:58","2017:01:02:23:59:58","Second"))
#     print('-='*30+'-')
