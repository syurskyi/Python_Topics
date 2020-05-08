from base_api import BaseApi
import xmltodict
import requests


class TestGetUserByLoginName(BaseApi):

    def test_get_user_by_login_name(self):
        url = self.base_url + '/user/' + self.settings['credentials']['login']

        r = self.request(url, 'get')

        self.assert_for_status_code_and_content_type(r, 200)
        self.validate_xml(r, 'xsd/user.xsd')

    def test_get_user_by_not_existing_login_name(self):
        url = self.base_url + '/user/' + 'smash'

        r = self.request(url, 'get')

        response_dict = xmltodict.parse(r.text)

        self.assert_for_status_code_and_content_type(r, 403)
        self.assertTrue(response_dict['error'])

    def test_get_user_by_login_name_without_credentials(self):
        url = self.base_url + '/user/' + self.settings['credentials']['login']

        r = requests.get(url)

        self.assert_for_status_code_and_content_type(r, 401)

        response_dict = xmltodict.parse(r.text)

        self.assertTrue(response_dict['error'])
