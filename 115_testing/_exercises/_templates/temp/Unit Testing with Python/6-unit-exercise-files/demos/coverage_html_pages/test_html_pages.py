______ u__
______ __
______ tempfile
______ io

____ html_pages ______ HtmlPagesConverter, FileAccessWrapper

c_ HtmlPagesTest?.?
    ___ test_inserts_br_tags_for_linebreaks
        filename _ __.pa__.join(tempfile.gettempdir(), "afile.txt")
        f _ o..(filename, "w", encoding_"UTF-8")
        f.write("plain text\n")
        f.close()
        converter _ HtmlPagesConverter(FileAccessWrapper(filename))
        new_text _ converter.get_html_page(0)
        aE..("plain text<br />", new_text)
        
    ___ test_quotes_escaped
        converter _ HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        new_text _ converter.get_html_page(0)
        aE..("text with &#x27;quotes&#x27;<br />", new_text)

    ___ test_random_access_pages
        converter _ HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two\nPAGE_BREAK\npage three"))
        page_two _ converter.get_html_page(1)
        aE..("page two<br />", page_two)

    ___ test_non_existant_file
        converter _ HtmlPagesConverter(FileAccessWrapper("missing"))
        aE..("", converter.get_html_page(0))

c_ FakeFileWrapper:
    ___  -   text
        text _ text
        
    ___ o..
        r_ io.StringIO(text)