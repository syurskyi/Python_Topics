# idea:
# sort all courses by deadline
# iterate all sorted courses
# if current course is able to be taken, then take it
# if not, check if we can remove some courses from courses we already taken
# if the one has the maximal duration is greater than current course's duration
# then replace it by current course
# since courses are already sorted by deadline, then our new deadline must be later
# (why? because sorted by deadline, current deadline must be later than all deadlines of taken courses, 
# so it must be valid)
# moreover, we have more available time for taking more courses

c_ Solution(object):
  ___ scheduleCourse  courses):
    """
    :type courses: List[List[int]]
    :rtype: int
    """
    now = 0
    heap    # list
    ___ t, d __ s..(courses, key=l.... x: x[1]):
      __ now + t <= d:
        now += t
        heapq.heappush(heap, -t)
      ____ heap a.. -heap[0] > t:
        now += t + heapq.heappop(heap)
        heapq.heappush(heap, -t)
    r.. l..(heap)
