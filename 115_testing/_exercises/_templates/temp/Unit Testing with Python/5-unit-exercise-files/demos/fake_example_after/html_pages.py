
______ html __ html_converter

c_ FileAccessWrapper:
    ___  -   filename
        filename _ filename
        
    ___ o..
        r_ o..(filename, "r", encoding_"UTF-8")

c_ HtmlPagesConverter:

    ___  -   file_access
        """Read the file and note the positions of the page breaks so we can access them quickly"""
        file_access _ file_access
        breaks _ [0]
        w__ file_access.o..() __ f:
            while True:
                line _ f.readline()
                __ not line:
                    break
                line _ line.rstrip()
                __ "PAGE_BREAK" in line:
                    page_break_position _ f.tell()
                    breaks.append(f.tell())
            breaks.append(f.tell())                

    ___ get_html_page  page
        """Return html page with the given number (zero indexed)"""
        page_start _ breaks[page]
        page_end _ breaks[page+1]
        html _ ""
        w__ file_access.o..() __ f:
            f.seek(page_start)
            while f.tell() !_ page_end:
                line _ f.readline()
                line _ line.rstrip()
                __ "PAGE_BREAK" in line:
                    continue
                html +_ html_converter.escape(line, quote_True)
                html +_ "<br />"
        r_ html

