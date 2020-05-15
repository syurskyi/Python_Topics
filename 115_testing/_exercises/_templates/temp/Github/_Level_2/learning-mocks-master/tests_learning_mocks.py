______ u__
____ u__ ______ mock, skip
____ u__.m.. ______ MagicMock

____ lxml ______ html
____ requests ______ Response

____ learning_mocks ______ FileRemovalService, UploadService, get_hrefs_from_url, filter_hrefs_by_text

# Followed along from https://www.toptal.com/python/an-introduction-to-mocking-in-python and
# https://blog.fugue.co/2016-02-11-python-mocking-101.html

c_ RmTestCase?.?

    @mock.patch('learning_mocks.os.path')
    @mock.patch('learning_mocks.os')
    ___ test_rm  mock_os, mock_path
        removal_service _ FileRemovalService()

        # set the condition for the mock
        mock_path.isfile.return_value _ F..
        removal_service.rm('any path')
        # test that remove call was NOT called
        aF..(mock_os.re...called, "Failed to NOT remove the if its not present")

        # set the condition that the file does exist for the mock
        mock_path.isfile.return_value _ T..
        removal_service.rm('any path')
        mock_os.re...a_c_w..('any path')


c_ UploadServiceTestCase?.?
    @mock.patch.object(FileRemovalService, 'rm')
    ___ test_upload_complete  mock_rm
        removal_service _ FileRemovalService()
        reference _ UploadService(removal_service)
        reference.upload_complete('my uploaded file')
        mock_rm.a_c_w..('my uploaded file')
        removal_service.rm.a_c_w..('my uploaded file')


c_ UploadServiceMockedTestCase?.?
    ___ test_upload_complete
        mock_removal_service _ mock.create_autospec(FileRemovalService)
        reference _ UploadService(mock_removal_service)
        reference.upload_complete('my uploaded file')
        mock_removal_service.rm.a_c_w..('my uploaded file')


c_ RequestsFunctionTests?.?
    ___ setUp
        page_content _ '<html><head><title>Some title</title></head><body>' \
                            '<a href="https://www.google.com/">Google</a>' \
                            '<a href="http://www.yahoo.com/">Yahoo</a>' \
                            '</body></html>'

    @mock.patch('learning_mocks.requests.get')
    ___ test_get_hrefs_from_url_calls_get  mock_request
        m_response _ MagicMock(spec_Response, status_code_200, text_page_content,
                               content_page_content)
        mock_request.return_value _ m_response
        get_hrefs_from_url('some url')
        mock_request.a_c_w..('some url')

    @mock.patch('learning_mocks.requests.get')
    ___ test_get_hrefs_from_url_returns_list  mock_get
        m_response _ mock.create_autospec(Response, content_page_content)
        mock_get.return_value _ m_response
        hrefs _ get_hrefs_from_url('some url')
        aT..(hasattr(hrefs, '__iter__'), 'No list returned')

    @mock.patch('learning_mocks.requests.get')
    ___ test_get_hrefs_from_url_returned_list_contains_text  mock_get
        m_response _ mock.create_autospec(Response, content_page_content)
        mock_get.return_value _ m_response
        hrefs _ get_hrefs_from_url('some url')
        good_search_string _ 'google'
        bad_search_string _ 'bad'
        aT..(any(good_search_string __ t ___ t __ hrefs),
                        'string {0} not found in list elements'.f..(good_search_string))
        aF..(any(bad_search_string __ t ___ t __ hrefs),
                         'found string "{0}" in list element when should NOT have been found'.f..(bad_search_string))


    ___ test_filter_hrefs_by_text_match_string_count
        # create a list to pass to function for testing
        web_element _ html.fromstring(page_content)
        href_list _ web_element.xpath('//a/@href')
        # filter the list with some different values
        yahoo_list _ filter_hrefs_by_text(href_list, 'yahoo')
        google_list _ filter_hrefs_by_text(href_list, 'google')
        google_fqdn_list _ filter_hrefs_by_text(href_list, 'www.google.com')
        yahoo_fqdn_list _ filter_hrefs_by_text(href_list, 'www.yahoo.com')
        filtered_lists _ [yahoo_list, yahoo_fqdn_list, google_list, google_fqdn_list]
        # test the filter results
        ___ fl __ filtered_lists:
            aT..(le.(fl), 1)

__ _____ __ ______
    ?.?