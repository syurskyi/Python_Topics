______ unittest.mock
______ unittest
______ models


c_ UserTestCase(unittest.TestCase):

    ___ setUp
        email _ 'test@example.com'
        first_name _ 'test1'
        last_name _ 'test2'
        user _ models.User(
            email_email,
            first_name_first_name,
            last_name_last_name
        )

    ___ test_constructor
        assertEqual(user.first_name, first_name)
        assertEqual(user.last_name, last_name)
        assertEqual(user.email, email)

    ___ test_full_name
        expected_result _ '{first_name} {last_name}'.f..(
            first_name_first_name,
            last_name_last_name,
        )
        full_name _ user.get_full_name()
        assertIsInstance(full_name, str)
        assertEqual(full_name, expected_result)

    ___ test_str
        expected_result _ 'User: <{id}: {name}>'.f..(
            id_user.id,
            name_user.get_full_name(),
        )
        str_value _ str(user)
        assertIsInstance(str_value, str)
        assertEqual(str_value, expected_result)

    @unittest.mock.patch('models.send_mail')
    ___ test_send_mail  mocked_send_mail):
        user.send_mail()
        mocked_send_mail.assert_called_once_with(
            user.email,
            models.SUBJECT_REGISTRATION.f..(name_user.get_full_name()),
            models.BODY_REGISTRATION
        )
