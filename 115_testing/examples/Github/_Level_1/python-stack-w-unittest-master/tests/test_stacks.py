import unittest

from stacks import Stack

class StackTestCase(unittest.TestCase):
    def test_is_empty_true(self):
        test_obj = Stack()
        self.assertEqual(True, test_obj.is_empty())

    def test_is_empty_false(self):
        test_obj = Stack()
        test_obj.push('data')
        self.assertEqual(False, test_obj.is_empty())

    def test_pop_handles_empty_stack(self):
        test_obj = Stack()
        self.assertEqual(None, test_obj.pop())
        self.assertEqual(True, test_obj.is_empty())

    def test_pop_pops_1_item_stack(self):
        test_obj = Stack()
        test_data = 'data1'
        test_obj.push(test_data)
        self.assertEqual(test_data, test_obj.pop())
        self.assertEqual(True, test_obj.is_empty())

    def test_pop_in_correct_order_from_2_item_stack(self):
        test_obj = Stack()
        test_data1 = 'data1'
        test_data2 = 'data2'
        test_obj.push(test_data1)
        test_obj.push(test_data2)
        self.assertEqual(test_data2, test_obj.pop())
        self.assertEqual(False, test_obj.is_empty())
        self.assertEqual(test_data1, test_obj.pop())
        self.assertEqual(True, test_obj.is_empty())

    def test_peek_handles_empty_stack(self):
        test_obj = Stack()
        self.assertEqual(None, test_obj.peek())
        self.assertEqual(True, test_obj.is_empty())

    def test_peek_shows_item_in_1_item_stack(self):
        test_obj = Stack()
        test_data = 'data1'
        test_obj.push(test_data)
        self.assertEqual(test_data, test_obj.peek())
        self.assertEqual(False, test_obj.is_empty())

    def test_peek_shows_top_of_2_item_stack(self):
        test_obj = Stack()
        test_data1 = 'data1'
        test_data2 = 'data2'
        test_obj.push(test_data1)
        test_obj.push(test_data2)
        self.assertEqual(test_data2, test_obj.peek())
        self.assertEqual(False, test_obj.is_empty())
        self.assertEqual(test_data2, test_obj.peek())

    def test_size_handles_empty_stack(self):
        test_obj = Stack()
        self.assertEqual(0, test_obj.size())
        self.assertEqual(True, test_obj.is_empty())

    def test_size_returns_1_for_1_item_stack(self):
        test_obj = Stack()
        test_data = 'data1'
        test_obj.push(test_data)
        self.assertEqual(1, test_obj.size())
        self.assertEqual(False, test_obj.is_empty())

    def test_size_returns_correct_number_for_many_item_stack(self):
        test_obj = Stack()
        test_data0 = 'data0'
        test_data1 = 'data1'
        test_data2 = 'data2'
        test_data3 = 'data3'
        test_data4 = 'data4'
        test_data5 = 'data5'
        test_data6 = 'data6'
        test_data7 = 'data7'
        test_data8 = 'data8'
        test_data9 = 'data9'
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
        self.assertEqual(10, test_obj.size())

if __name__ == '__main__':
    unittest.main()
