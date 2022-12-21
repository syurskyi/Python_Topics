"""
只能用递归不能用其他数据结构来逆序一个栈。

可以用另一个新栈的话比较容易。

"""


from GetMinStack import Stack


___ reverseStack(stacks
    new_stack = Stack()

    ___ helper(stacks
        __ stacks.empty(
            r_

        new_stack.push(stacks.pop())

        helper(stacks)

    helper(stacks)

    r_ new_stack

# 测试用例。
a = r..(10)

b = Stack()

___ i __ a:
    b.push(i)

# 不用assert了。
print(b)

print(reverseStack(b))


