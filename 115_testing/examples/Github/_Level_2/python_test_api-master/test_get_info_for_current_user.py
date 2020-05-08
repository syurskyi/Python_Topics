from base_api import BaseApi
import xmltodict
import requests


class TestGetInfoForCurrentUser(BaseApi):

    def test_get_info_for_current_user(self):
        url = self.base_url + '/user/current'

        r = self.request(url, 'get')

        self.assert_for_status_code_and_content_type(r, 200)
        self.validate_xml(r, 'xsd/user.xsd')

    def test_get_info_for_current_user_without_credentials(self):
        url = self.base_url + '/user/current'

        r = requests.get(url)

        self.assert_for_status_code_and_content_type(r, 200)

        response_dict = xmltodict.parse(r.text)

        self.assertTrue(response_dict['user'])
        self.assertEqual(response_dict['user']['@login'], '<no user>')
        self.assertEqual(response_dict['user']['@guest'], 'false')
