c_ MyQueue:
    ___ - , ):
        stack1    # list
        stack2    # list

    """
    @param: element: An integer
    @return: nothing
    """
    ___ push(self, element):
        stack1.a..(element)

    """
    @return: An integer
    """
    ___ pop(self, ):
        top()
        r.. stack2.pop()

    """
    @return: An integer
    """
    ___ top(self, ):
        # While `self.stack2` is empty, get element from `self.stack1`
        # step0/ stack1: [1, 2, 3], stack2: []
        # step1/ stack1: [], stack2: [3, 2, 1]
        # step2/ stack1: [4, 5, 6], stack2: [3, 2] // 1
        # step3/ stack1: [4, 5, 6], stack2: [] // 2, 3
        # step4/ stack1: [7, 8], stack2: [6, 5, 4]
        __ n.. stack2:
            w.... stack1:
                stack2.a..(stack1.pop())
        r.. stack2[-1]
