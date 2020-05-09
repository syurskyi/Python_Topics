____ django.test ______ TestCase
____ django.contrib.auth.models ______ User
____ django.urls ______ reverse
____ rest_framework ______ status


c_ AuthApiTestCase(TestCase

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

    ___ test_auth_login_endpoint
        credentials _ {
            'username': username,
            'password': password,
        }
        url _ reverse('auth-login')
        response _ client.post(url, data_credentials,
                                    content_type_'application/json')
        assertTrue(response.status_code, status.HTTP_200_OK)
        expected_response _ {'details': 'You successfully logged in'}
        assertDictEqual(response.data, expected_response)

    ___ test_auth_login_endpoint_without_username
        credentials _ {
            'password': password,
        }
        url _ reverse('auth-login')
        response _ client.post(url, data_credentials,
                                    content_type_'application/json')
        assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        assertIn('username', response.data)

    ___ test_auth_login_endpoint_without_password
        credentials _ {
            'username': username,
        }
        url _ reverse('auth-login')
        response _ client.post(url, data_credentials,
                                    content_type_'application/json')
        assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        assertIn('password', response.data)

    ___ test_auth_login_endpoint_without_data
        credentials _ {}
        url _ reverse('auth-login')
        response _ client.post(url, data_credentials,
                                    content_type_'application/json')
        assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_keys _ list(response.data.keys())
        assertListEqual(['username', 'password'], error_keys)

    ___ test_auth_login_endpoint_with_wrong_credentials
        credentials _ {
            'username': 'wrong_username',
            'password': 'wrong_password',
        }
        url _ reverse('auth-login')
        response _ client.post(url, data_credentials,
                                    content_type_'application/json')
        assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_keys _ list(response.data.keys())
        assertListEqual(['non_field_errors'], error_keys)
        assertListEqual(['non_field_errors'], error_keys)
        aE..(response.data['non_field_errors'][0],
                         'Incorrect username/password')
