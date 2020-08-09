from nose.tools ______ assert_equal


class TestPalindrome(object

    ___ test_palindrome(self
        print('Test: Empty list')
        linked_list = MyLinkedList()
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        assert_equal(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        assert_equal(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


___ main(
    test = TestPalindrome()
    test.test_palindrome()


__ __name__ __ '__main__':
    main()