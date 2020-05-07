from base_api import BaseApi
import xmltodict
import requests


class TestGetListOfIssues(BaseApi):

    def test_get_list_of_issues(self):
        url = self.base_url + '/issue'

        params = {
            'with': 'Priority',
            'max': '10',
            'after': '20'
        }

        r = self.request(url, 'get', params)

        response_dict = xmltodict.parse(r.text)

        self.assert_for_status_code_and_content_type(r, 200)
        for x in response_dict['issueCompacts']['issue']:
            self.assertTrue(x['@id'])

    def test_get_list_of_issues_without_credentials(self):
        url = self.base_url + '/issue'

        params = {
            'with': 'Priority',
            'max': '10',
            'after': '20'
        }

        r = requests.get(url, params)

        self.assert_for_status_code_and_content_type(r, 401)

        response_dict = xmltodict.parse(r.text)

        self.assertTrue(response_dict['error'])
