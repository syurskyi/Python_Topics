______ random
____ unittest ______ TestCase
____ unittest.mock ______ Mock, patch


c_ TestMyObject(TestCase):
    """
    Showcase for using mocks in unittest
    """

    # creating a mock without annotations
    ___ test_random_mock
        random.randint _ Mock(return_value_3)
        assertEqual(3, random.randint(1, 10))

    # mock two methods and define the return value
    @patch('random.seed')
    @patch('random.randint')
    ___ test_random_patch  random_mock, seed_mock):
        random_mock.return_value _ 3
        assertEqual(3, random.randint(1, 10))
        random_mock.assert_called_with(1, 10)
        random_mock.assert_called_once_with(1, 10)
        seed_mock.assert_not_called()

    # mock a method a create a side effect
    @patch('random.randint')
    ___ test_side_effect  random_mock):
        random_mock.side_effect _ Exception('Random value exception')
        assertEqual(3, random.randint(1, 10))
