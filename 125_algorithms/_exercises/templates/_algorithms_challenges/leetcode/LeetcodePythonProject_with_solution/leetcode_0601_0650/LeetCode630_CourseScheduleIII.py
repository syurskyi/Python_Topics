'''
Created on Sep 12, 2017

@author: MT
'''
c_ Solution(o..
    ___ scheduleCourse  courses
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        _______ heapq
        heap    # list
        courses.s..(key=l.... x: x[1])
        t__ 0
        ___ course __ courses:
            t__ += course[0]
            heapq.heappush(heap, -course 0
            __ t__ > course[1]:
                t__ -_ -heapq.heappop(heap)
        r.. l..(heap)
    
    ___ test
        testCases [
            [[1,2]],
            [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],
            [[5, 5], [4, 6], [2, 6]],
            [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]],
        ]
        ___ courses __ testCases:
            print('courses: %s' % courses)
            result scheduleCourse(courses)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
