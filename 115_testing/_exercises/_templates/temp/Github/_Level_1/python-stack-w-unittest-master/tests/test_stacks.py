______ unittest

____ stacks ______ Stack

c_ StackTestCase(unittest.TestCase):
    ___ test_is_empty_true
        test_obj _ Stack()
        assertEqual(True, test_obj.is_empty())

    ___ test_is_empty_false
        test_obj _ Stack()
        test_obj.push('data')
        assertEqual(False, test_obj.is_empty())

    ___ test_pop_handles_empty_stack
        test_obj _ Stack()
        assertEqual(None, test_obj.pop())
        assertEqual(True, test_obj.is_empty())

    ___ test_pop_pops_1_item_stack
        test_obj _ Stack()
        test_data _ 'data1'
        test_obj.push(test_data)
        assertEqual(test_data, test_obj.pop())
        assertEqual(True, test_obj.is_empty())

    ___ test_pop_in_correct_order_from_2_item_stack
        test_obj _ Stack()
        test_data1 _ 'data1'
        test_data2 _ 'data2'
        test_obj.push(test_data1)
        test_obj.push(test_data2)
        assertEqual(test_data2, test_obj.pop())
        assertEqual(False, test_obj.is_empty())
        assertEqual(test_data1, test_obj.pop())
        assertEqual(True, test_obj.is_empty())

    ___ test_peek_handles_empty_stack
        test_obj _ Stack()
        assertEqual(None, test_obj.peek())
        assertEqual(True, test_obj.is_empty())

    ___ test_peek_shows_item_in_1_item_stack
        test_obj _ Stack()
        test_data _ 'data1'
        test_obj.push(test_data)
        assertEqual(test_data, test_obj.peek())
        assertEqual(False, test_obj.is_empty())

    ___ test_peek_shows_top_of_2_item_stack
        test_obj _ Stack()
        test_data1 _ 'data1'
        test_data2 _ 'data2'
        test_obj.push(test_data1)
        test_obj.push(test_data2)
        assertEqual(test_data2, test_obj.peek())
        assertEqual(False, test_obj.is_empty())
        assertEqual(test_data2, test_obj.peek())

    ___ test_size_handles_empty_stack
        test_obj _ Stack()
        assertEqual(0, test_obj.size())
        assertEqual(True, test_obj.is_empty())

    ___ test_size_returns_1_for_1_item_stack
        test_obj _ Stack()
        test_data _ 'data1'
        test_obj.push(test_data)
        assertEqual(1, test_obj.size())
        assertEqual(False, test_obj.is_empty())

    ___ test_size_returns_correct_number_for_many_item_stack
        test_obj _ Stack()
        test_data0 _ 'data0'
        test_data1 _ 'data1'
        test_data2 _ 'data2'
        test_data3 _ 'data3'
        test_data4 _ 'data4'
        test_data5 _ 'data5'
        test_data6 _ 'data6'
        test_data7 _ 'data7'
        test_data8 _ 'data8'
        test_data9 _ 'data9'
        test_obj.push(test_data0)
        test_obj.push(test_data1)
        test_obj.push(test_data2)
        test_obj.push(test_data3)
        test_obj.push(test_data4)
        test_obj.push(test_data5)
        test_obj.push(test_data6)
        test_obj.push(test_data7)
        test_obj.push(test_data8)
        test_obj.push(test_data9)
        assertEqual(10, test_obj.size())

if __name__ == '__main__':
    unittest.main()
