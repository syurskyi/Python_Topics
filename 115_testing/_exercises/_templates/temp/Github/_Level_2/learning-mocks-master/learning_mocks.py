______ __

______ re
______ requests
____ selenium ______ webdriver
____ lxml ______ html

c_ FileRemovalService(object
    ___ rm  filename
        __ __.pa__.isfile(filename
            __.remove(filename)


c_ UploadService(object

    ___  -   removal_service
        removal_service _ removal_service

    ___ upload_complete  filename
        removal_service.rm(filename)


___ rm(filename
    __ __.pa__.isfile(filename
        __.remove(filename)

___ get_hrefs_from_url(url
    page _ requests.get(url)
    content _ html.fromstring(page.content)
    r_ content.xpath('//a/@href')


___ filter_hrefs_by_text(hrefs_list, filter_string
    regex _ re.compile('^http[s]?://\S*{0}\S*'.f..(filter_string))
    r_ [h for h in hrefs_list __ regex.search(h)]

___ main(
    pass


__ __name__ == "__main__":
    main()
