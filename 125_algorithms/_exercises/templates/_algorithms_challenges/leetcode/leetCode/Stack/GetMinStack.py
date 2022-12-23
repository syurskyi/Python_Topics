"""
设计一个可以 Get Min的栈结构。

栈是一个先进后出的数据结构。

要设计这样的一个需要两个栈来完成，一个栈用于正常的存储，另一个用于只存储最小的。

这样push/pop get min都是O(1) 时间完成。

非常基础。

其实在Python中可以用类直接写min属性，不过限定了只能用栈了。

"""

# deque 是一个Python实现的双端队列。
# 由底层C代码实现。
# 使用它可以保证在左右两端进行添加和删除操作时间都是O(1)。
from collections import deque

testStack = r..(10)


c.. Stack:
    """
        一个先进后出的栈。
    """
    ___ __init__(self
        """
            这里用实例对象。
        """
        self.stored = deque()

    ___ __repr__(self
        # 3.6 +
        r_ f'<{self.stored}>'

    ___ push  value
        self.stored.a.. value)

    ___ pop(self
        r_ self.stored.pop()

    ___ get_top(self
        """
            查看栈顶的数据但不压出。
        """
        r_ self.stored[-1]

    ___ empty(self
        __ self.stored:
            r_ False
        r_ True


c.. MinStack(Stack
    """
        一个可以在O(1)时间内获取出最小值的栈。
    """
    ___ __init__(self
        super().__init__()

        self.minStack = Stack()

    ___ push  value
        super().push(value)
        __ self.minStack.empty(
            self.minStack.push(value)
        ____
            __ self.minStack.get_top() <= value:
                self.minStack.push(self.minStack.get_top())
            ____
                self.minStack.push(value)

    ___ pop(self
        super().pop()
        self.minStack.pop()

    ___ get_min(self
        """
            返回栈顶但不压出。
        """
        r_ self.minStack.get_top()


a = Stack()
___ i __ testStack:
    a.push(i)

print(a)
a.pop()
print(a)

a = MinStack()

a.push(1)
print(a.get_min()) # 1
a.push(2) 
print(a.get_min()) # 1
a.push(0)
print(a.get_min()) # 0
a.pop()
print(a.get_min()) # 1

