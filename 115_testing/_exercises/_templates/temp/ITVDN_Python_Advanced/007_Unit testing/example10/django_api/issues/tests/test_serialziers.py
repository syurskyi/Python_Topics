____ django.test ______ TestCase
____ django.contrib.auth.models ______ User

____ issues.serializers ______ LoginSerializer


c_ LoginSerializerTestCase(TestCase

    ___ setUp
        username _ 'test'
        password _ 'pass1234'
        user _ User.objects.create_user(
            first_name_'Test',
            last_name_'Testovich',
            username_username,
            password_password,
            email_'test@example.com'
        )

    ___ test_validate_with_wrong_credentials
        credentials _ {
            'username': 'test1',
            'password': 'pass'
        }
        serializer _ LoginSerializer(data_credentials)
        assertFalse(serializer.is_valid())
        assertGreater(len(serializer.errors), 0)
        assertRegex(serializer.errors['non_field_errors'][0],
                         'Incorrect username\/password')

    ___ test_validate_without_password
        credentials _ {
            'username': 'test1',
        }
        serializer _ LoginSerializer(data_credentials)
        assertFalse(serializer.is_valid())
        assertIn('password', serializer.errors)
        assertRegex(serializer.errors['password'][0],
                         'required')

    ___ test_validate_without_username
        credentials _ {
            'password': 'pass',
        }
        serializer _ LoginSerializer(data_credentials)
        assertFalse(serializer.is_valid())
        assertIn('username', serializer.errors)
        assertRegex(serializer.errors['username'][0],
                         'required')

    ___ test_validate
        credentials _ {
            'username': username,
            'password': password,
        }
        serializer _ LoginSerializer(data_credentials)
        assertTrue(serializer.is_valid())
        AII..(serializer.validated_data, User)
