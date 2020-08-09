'''
Created on Sep 12, 2017

@author: MT
'''
class Solution(object
    ___ scheduleCourse(self, courses
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        ______ heapq
        heap = []
        courses.sort(key=lambda x: x[1])
        time = 0
        ___ course in courses:
            time += course[0]
            heapq.heappush(heap, -course[0])
            __ time > course[1]:
                time -= -heapq.heappop(heap)
        r_ le.(heap)
    
    ___ test(self
        testCases = [
            [[1,2]],
            [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],
            [[5, 5], [4, 6], [2, 6]],
            [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]],
        ]
        ___ courses in testCases:
            print('courses: %s' % courses)
            result = self.scheduleCourse(courses)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
