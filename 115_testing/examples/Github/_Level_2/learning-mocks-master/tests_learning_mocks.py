import unittest
from unittest import mock, skip
from unittest.mock import MagicMock

from lxml import html
from requests import Response

from learning_mocks import FileRemovalService, UploadService, get_hrefs_from_url, filter_hrefs_by_text

# Followed along from https://www.toptal.com/python/an-introduction-to-mocking-in-python and
# https://blog.fugue.co/2016-02-11-python-mocking-101.html

class RmTestCase(unittest.TestCase):

    @mock.patch('learning_mocks.os.path')
    @mock.patch('learning_mocks.os')
    def test_rm(self, mock_os, mock_path):
        removal_service = FileRemovalService()

        # set the condition for the mock
        mock_path.isfile.return_value = False
        removal_service.rm('any path')
        # test that remove call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed to NOT remove the if its not present")

        # set the condition that the file does exist for the mock
        mock_path.isfile.return_value = True
        removal_service.rm('any path')
        mock_os.remove.assert_called_with('any path')


class UploadServiceTestCase(unittest.TestCase):
    @mock.patch.object(FileRemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        removal_service = FileRemovalService()
        reference = UploadService(removal_service)
        reference.upload_complete('my uploaded file')
        mock_rm.assert_called_with('my uploaded file')
        removal_service.rm.assert_called_with('my uploaded file')


class UploadServiceMockedTestCase(unittest.TestCase):
    def test_upload_complete(self):
        mock_removal_service = mock.create_autospec(FileRemovalService)
        reference = UploadService(mock_removal_service)
        reference.upload_complete('my uploaded file')
        mock_removal_service.rm.assert_called_with('my uploaded file')


class RequestsFunctionTests(unittest.TestCase):
    def setUp(self):
        self.page_content = '<html><head><title>Some title</title></head><body>' \
                            '<a href="https://www.google.com/">Google</a>' \
                            '<a href="http://www.yahoo.com/">Yahoo</a>' \
                            '</body></html>'

    @mock.patch('learning_mocks.requests.get')
    def test_get_hrefs_from_url_calls_get(self, mock_request):
        m_response = MagicMock(spec=Response, status_code=200, text=self.page_content,
                               content=self.page_content)
        mock_request.return_value = m_response
        get_hrefs_from_url('some url')
        mock_request.assert_called_with('some url')

    @mock.patch('learning_mocks.requests.get')
    def test_get_hrefs_from_url_returns_list(self, mock_get):
        m_response = mock.create_autospec(Response, content=self.page_content)
        mock_get.return_value = m_response
        hrefs = get_hrefs_from_url('some url')
        self.assertTrue(hasattr(hrefs, '__iter__'), 'No list returned')

    @mock.patch('learning_mocks.requests.get')
    def test_get_hrefs_from_url_returned_list_contains_text(self, mock_get):
        m_response = mock.create_autospec(Response, content=self.page_content)
        mock_get.return_value = m_response
        hrefs = get_hrefs_from_url('some url')
        good_search_string = 'google'
        bad_search_string = 'bad'
        self.assertTrue(any(good_search_string in t for t in hrefs),
                        'string {0} not found in list elements'.format(good_search_string))
        self.assertFalse(any(bad_search_string in t for t in hrefs),
                         'found string "{0}" in list element when should NOT have been found'.format(bad_search_string))


    def test_filter_hrefs_by_text_match_string_count(self):
        # create a list to pass to function for testing
        web_element = html.fromstring(self.page_content)
        href_list = web_element.xpath('//a/@href')
        # filter the list with some different values
        yahoo_list = filter_hrefs_by_text(href_list, 'yahoo')
        google_list = filter_hrefs_by_text(href_list, 'google')
        google_fqdn_list = filter_hrefs_by_text(href_list, 'www.google.com')
        yahoo_fqdn_list = filter_hrefs_by_text(href_list, 'www.yahoo.com')
        filtered_lists = [yahoo_list, yahoo_fqdn_list, google_list, google_fqdn_list]
        # test the filter results
        for fl in filtered_lists:
            self.assertTrue(len(fl), 1)

if __name__ == "__main__":
    unittest.main()