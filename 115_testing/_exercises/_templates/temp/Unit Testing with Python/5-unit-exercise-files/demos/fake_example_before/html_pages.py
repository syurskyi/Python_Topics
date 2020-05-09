
______ html __ html_converter

c_ HtmlPagesConverter:

    ___  -   filename
        """Read the file and note the positions of the page breaks so we can access them quickly"""
        filename _ filename
        breaks _ [0]
        w__ o..(filename, "r", encoding_"UTF-8") __ f:
            while T..:
                line _ f.readline()
                __ no. line:
                    break
                line _ line.rstrip()
                __ "PAGE_BREAK" in line:
                    page_break_position _ f.tell()
                    breaks.a..(f.tell())
            breaks.a..(f.tell())

    ___ get_html_page  page
        """Return html page with the given number (zero indexed)"""
        page_start _ breaks[page]
        page_end _ breaks[page+1]
        html _ ""
        w__ o..(filename, "r", encoding_"UTF-8") __ f:
            f.seek(page_start)
            while f.tell() !_ page_end:
                line _ f.readline()
                line _ line.rstrip()
                __ "PAGE_BREAK" in line:
                    continue
                html +_ html_converter.escape(line, quote_True)
                html +_ "<br />"
        r_ html

