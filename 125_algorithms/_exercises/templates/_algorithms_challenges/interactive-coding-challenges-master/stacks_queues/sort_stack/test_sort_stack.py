from random ______ randint
from nose.tools ______ assert_equal


class TestSortStack(object

    ___ get_sorted_stack(self, stack, numbers
        ___ x in numbers:
            stack.push(x)
        sorted_stack = stack.sort()
        r_ sorted_stack

    ___ test_sort_stack(self, stack
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack(stack, [])
        assert_equal(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack(stack, [1])
        assert_equal(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) ___ x in range(num_items)]
        sorted_stack = self.get_sorted_stack(stack, numbers)
        sorted_numbers = []
        ___ _ in range(num_items
            sorted_numbers.append(sorted_stack.pop())
        assert_equal(sorted_numbers, sorted(numbers, reverse=True))

        print('Success: test_sort_stack')


___ main(
    test = TestSortStack()
    test.test_sort_stack(MyStack())
    test.test_sort_stack(MyStackSimplified())


__ __name__ __ '__main__':
    main()