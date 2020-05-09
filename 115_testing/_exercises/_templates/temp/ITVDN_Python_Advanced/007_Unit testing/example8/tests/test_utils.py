______ unittest
____ utils ______ send_mail, concat_name, set_user_meta
____ models ______ User


c_ UtilsTestCase(unittest.TestCase):

    ___ test_concat_name
        value1, value2 _ 'test1', 'test2'
        result _ concat_name(value1, value2)
        expected_result _ '{} {}'.f..(value1, value2)
        assertEqual(result, expected_result)

    ___ test_set_user_meta
        instance _ User('test@example.com', '1', '2')
        test_meta _ {'test_key': 'test_value'}
        set_user_meta(instance, test_meta)
        assertDictEqual(instance.meta, test_meta)
